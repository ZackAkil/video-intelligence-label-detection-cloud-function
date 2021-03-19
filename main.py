from google.cloud import videointelligence_v1p3beta1 as videointelligence


OUTPUT_BUCKET = 'gs://YOUR OUTPUT BUCKET/'

client = videointelligence.VideoIntelligenceServiceClient()

# Optional: define extra settings for label detection
config = videointelligence.types.LabelDetectionConfig(label_detection_mode=videointelligence.LabelDetectionMode.SHOT_MODE,
                                                      video_confidence_threshold = 0.5)

video_context = videointelligence.types.VideoContext(label_detection_config=config)

def analyse(event, context):
  
    print(event)

    gcs_uri = 'gs://' + event['bucket'] + '/' + event['name']
    just_file_name = event['name'].split('.')[0]

    operation = client.annotate_video({
      'input_uri': gcs_uri,
      'features':[videointelligence.Feature.LABEL_DETECTION],
      'output_uri':  OUTPUT_BUCKET + just_file_name + '.json',
      'video_context': video_context
    })
    
    print("\nProcessing video for label detection.")
