import json, pathlib
p=pathlib.Path(__file__).parents[1]/'schemas'
p.mkdir(exist_ok=True)
S=lambda **kwargs: dict(type='string',**kwargs)
str1=S(minLength=1)
idea={
 '$schema':'https://json-schema.org/draft/2020-12/schema',
 'title':'Dr Marvin Idea v1','type':'object','additionalProperties':False,
 'required':['idea_id','name','aliases','problem','existing_workaround','mechanism','madness','visual_concept','novelty_note','scores','status','tags','related_ids','post_id','post_packet_path'],
 'properties':{
   'idea_id':S(pattern=r'^MM-I\d{4}$'), 'name':str1, 'aliases':{'type':'array','items':S()},
   'problem':str1,'existing_workaround':str1,'mechanism':str1,'madness':str1,'visual_concept':str1,
   'novelty_note':str1,
   'scores':{'type':'object','additionalProperties':False,'required':['relatability','ingenuity','madness','visual_clarity','shareability','product_desire'],
      'properties':{k:{'type':'integer','minimum':1,'maximum':5} for k in ['relatability','ingenuity','madness','visual_clarity','shareability','product_desire']}},
   'status':{'enum':['PROPOSED','SELECTED','PACKAGED','ILLUSTRATED','RENDERED','PUBLISHED','HOLD','REJECTED']},
   'tags':{'type':'array','items':S()},'related_ids':{'type':'array','items':S(pattern=r'^MM-I\d{4}$')},
   'post_id':{'type':['string','null'],'pattern':r'^MM-P\d{4}$'},
   'post_packet_path':{'type':['string','null']},
   'published_url':{'type':['string','null']},
   'published_date':{'type':['string','null']},
   'editorial_notes':S()
 }
}
registry={
 '$schema':'https://json-schema.org/draft/2020-12/schema',
 'title':'Dr Marvin Registry v1','type':'object','additionalProperties':False,
 'required':['schema_version','brand','next_idea_number','next_post_number','ideas'],
 'properties':{
 'schema_version':{'const':'dmmm_registry_v1'},
 'brand':{'const':"Dr. Marvin's Marvelous Machines"},
 'next_idea_number':{'type':'integer','minimum':1},
 'next_post_number':{'type':'integer','minimum':1},
 'ideas':{'type':'array','items':{'$ref':'idea.schema.json'}}
 }
}
feature={
 'type':'object','additionalProperties':False,'required':['title','explanation'],
 'properties':{'title':S(minLength=3,maxLength=60),'explanation':S(minLength=15,maxLength=190)}
}
post={
 '$schema':'https://json-schema.org/draft/2020-12/schema',
 'title':'Dr Marvin Four-Slide Packet v1','type':'object','additionalProperties':False,
 'required':['schema_version','idea_id','post_id','revision','brand','canvas','title','engineering','art_brief','slides','caption','lifecycle','qa'],
 'properties':{
  'schema_version':{'const':'dmmm_post_v1'},
  'idea_id':S(pattern=r'^MM-I\d{4}$'),
  'post_id':S(pattern=r'^MM-P\d{4}$'),
  'revision':{'type':'integer','minimum':1},
  'brand':{'const':"Dr. Marvin's Marvelous Machines"},
  'canvas':{'type':'object','additionalProperties':False,'required':['width','height','slide_count'],
     'properties':{'width':{'const':1080},'height':{'const':1350},'slide_count':{'const':4}}},
  'title':S(minLength=4,maxLength=100),
  'engineering':{'type':'object','additionalProperties':False,
   'required':['annoyance','current_workaround','object_form','operating_principle','mechanism_assumptions','tradeoff','novelty_note'],
   'properties':{k:str1 for k in ['annoyance','current_workaround','object_form','operating_principle','mechanism_assumptions','tradeoff','novelty_note']}},
  'art_brief':{'type':'object','additionalProperties':False,'required':['prompt','alt_text','asset_uri','approved'],
    'properties':{'prompt':S(minLength=220),'alt_text':S(minLength=10,maxLength=280),
       'asset_uri':{'type':['string','null']},'approved':{'type':'boolean'}}},
  'slides':{'type':'object','additionalProperties':False,'required':['slide_1','slide_2','slide_3','slide_4'],
   'properties':{
    'slide_1':{'type':'object','additionalProperties':False,'required':['type','header','title','hook','concept_label'],
     'properties':{'type':{'const':'invention'},'header':{'const':"FROM DR. MARVIN'S LABORATORY"},'title':S(minLength=4,maxLength=100),'hook':S(minLength=10,maxLength=180),'concept_label':{'const':'CONCEPT DESIGN'}}},
    'slide_2':{'type':'object','additionalProperties':False,'required':['type','header','heading','body'],
      'properties':{'type':{'const':'problem'},'header':{'const':'A MOST DREADFUL PROBLEM'},'heading':S(minLength=5,maxLength=85),'body':S(minLength=50,maxLength=650)}},
    'slide_3':{'type':'object','additionalProperties':False,'required':['type','header','mechanical_thesis','features'],
      'properties':{'type':{'const':'solution'},'header':{'const':'THE STROKE OF GENIUS'},'mechanical_thesis':S(maxLength=175),
      'features':{'type':'array','minItems':3,'maxItems':3,'items':feature}}},
    'slide_4':{'type':'object','additionalProperties':False,'required':['type','header','question','left_verdict','right_verdict','comment_cta'],
     'properties':{'type':{'const':'verdict'},'header':{'const':'GENIUS OR MADNESS?'},'question':S(minLength=20,maxLength=250),
      'left_verdict':{'const':'GENIUS'},'right_verdict':{'const':'MADNESS'},'comment_cta':{'const':'CAST YOUR VERDICT IN THE COMMENTS'}}}
    }},
  'caption':S(minLength=30,maxLength=750),
  'lifecycle':{'type':'object','additionalProperties':False,'required':['status','published_url','published_date','artwork_references','export_references'],
    'properties':{
     'status':{'enum':['PACKAGED','ILLUSTRATED','RENDERED','PUBLISHED']},
     'published_url':{'type':['string','null']},'published_date':{'type':['string','null']},
     'artwork_references':{'type':'array','items':S()},
     'export_references':{'type':'array','items':S()}}},
  'qa':{'type':'object','additionalProperties':False,'required':['editorial_review','mechanism_review','claims_review','render_review','review_notes'],
    'properties':{
     'editorial_review':{'enum':['PASS','NEEDS_REVISION','NOT_RUN']},
     'mechanism_review':{'enum':['PASS','NEEDS_REVISION','NOT_RUN']},
     'claims_review':{'enum':['PASS','NEEDS_REVISION','NOT_RUN']},
     'render_review':{'enum':['PASS','BLOCKED_NOT_RENDERED','NEEDS_REVISION','NOT_RUN']},
     'review_notes':S()}}
 }
}
for name,obj in [('idea.schema.json',idea),('registry.schema.json',registry),('post-packet.schema.json',post)]:
 (p/name).write_text(json.dumps(obj,indent=2,ensure_ascii=False)+'\n')
print('created schemas')
