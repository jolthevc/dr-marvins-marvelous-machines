#!/usr/bin/env python3
"""Validate repo JSON documents and editorial contract. Requires jsonschema for full checks.

Usage: python tools/validate.py
Install jsonschema if needed: python -m pip install jsonschema
"""
import json
from pathlib import Path
from collections import Counter

ROOT = Path(__file__).resolve().parents[1]

def load(rel):
    return json.loads((ROOT / rel).read_text(encoding='utf-8'))

def main():
    errors=[]
    try:
        import jsonschema
    except ImportError:
        jsonschema=None
        print('WARNING: jsonschema unavailable; checking semantic invariants and JSON syntax only.')
    registry=load('ideas/registry.json')
    r_schema=load('schemas/registry.schema.json')
    p_schema=load('schemas/post-packet.schema.json')
    i_schema=load('schemas/idea.schema.json')
    if jsonschema:
        resolver=jsonschema.RefResolver.from_schema(r_schema,store={'idea.schema.json':i_schema})
        try: jsonschema.validate(registry,r_schema,resolver=resolver)
        except Exception as ex: errors.append(f'registry schema: {ex}')
    ids=[x['idea_id'] for x in registry['ideas']]
    for i,c in Counter(ids).items():
        if c>1: errors.append(f'duplicate idea id: {i}')
    post_ids=[x.get('post_id') for x in registry['ideas'] if x.get('post_id')]
    for i,c in Counter(post_ids).items():
        if c>1: errors.append(f'duplicate post id: {i}')
    if registry['ideas']:
        max_id=max(int(x[4:]) for x in ids)
        if registry['next_idea_number']<=max_id: errors.append('next_idea_number not ahead of existing ids')
    packets=list((ROOT/'posts').glob('*.packet.json'))+list((ROOT/'examples').glob('*.packet.json'))
    for path in packets:
        try: p=json.loads(path.read_text(encoding='utf-8'))
        except Exception as ex:
            errors.append(f'{path}: {ex}');continue
        if jsonschema:
            try: jsonschema.validate(p,p_schema)
            except Exception as ex: errors.append(f'{path.name} schema: {ex}')
        if p['slides']['slide_1']['title']!=p['title']: errors.append(f'{path.name}: title mismatch')
        if len(p['slides']['slide_3']['features'])!=3: errors.append(f'{path.name}: require 3 features')
        if p['art_brief']['asset_uri'] is None and p['lifecycle']['status'] in ('ILLUSTRATED','RENDERED','PUBLISHED'):
            errors.append(f'{path.name}: claimed illustrated without art uri')
        if p['lifecycle']['status'] in ('RENDERED','PUBLISHED') and len(p['lifecycle']['export_references'])!=4:
            errors.append(f'{path.name}: claimed rendered without 4 export refs')
        if p['lifecycle']['status']=='PUBLISHED' and not p['lifecycle']['published_url']:
            errors.append(f'{path.name}: claimed published without url')
        for key in ('slide_1','slide_2','slide_3','slide_4'):
            if '\u2014' in json.dumps(p['slides'][key],ensure_ascii=False): errors.append(f'{path.name}: em dash in {key}')
        if '\u2014' in p['caption']: errors.append(f'{path.name}: em dash in caption')
    if errors:
        print('FAILED:')
        print('\n'.join(' - '+x for x in errors))
        raise SystemExit(1)
    print(f'PASS: registry ({len(ids)} ideas), {len(packets)} packet(s), IDs and lifecycle invariants.')
    if not jsonschema: print('NOTE: install jsonschema for complete schema validation.')

if __name__=='__main__': main()
