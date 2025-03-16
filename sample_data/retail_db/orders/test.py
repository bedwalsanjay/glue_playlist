import json
event= {
   "Records":[
      {
         "messageId":"000a29ac-c63f-4ad9-b259-f7c8d646ea0a",
         "receiptHandle":"AQEBHR94K6Nfj3ICsG7K2/8+ZikStNCd/Q85Jk9mI4dmzgf1mGU0ofhfRpA5wY6vHh5A/spheKm9OKGaQz7B+SSjdh2UajwwG4qtwFBLS1q4z+lggxgMyPjsFMByjhHcCt5jT+stX+xAqTLGHz9r6MFFovtM/5RkKz4NKmBx5ZbjQdIkY360zWXofIEvVCPrdPr8EpWh4ol8Si5QKimVcrjvauzvvDkta+3632kf7BbiYyublTJM9EQhYkc3yCQ4jrPWZ6z22HmIcOdH9hQFzAZyugT3D8ADJcU0Kf9KPWWgIQS1k2IzuW8eFWxTpZgh10UZjtNWxjVPLS/fmDOzM/oHJa4CqPOE4t070RleuC5lLGw8YuH/RLECQRd51u/zptYbatDlu6ErAolFu/J6GpVQRg==",
         "body":"{\n  \"Type\" : \"Notification\",\n  \"MessageId\" : \"8bbb1344-a737-5e12-bddc-4e1376ed358d\",\n  \"TopicArn\" : \"arn:aws:sns:ap-south-1:526844078262:sb_topic\",\n  \"Subject\" : \"Amazon S3 Notification\",\n  \"Message\" : \"{\\\"Records\\\":[{\\\"eventVersion\\\":\\\"2.1\\\",\\\"eventSource\\\":\\\"aws:s3\\\",\\\"awsRegion\\\":\\\"ap-south-1\\\",\\\"eventTime\\\":\\\"2023-08-17T07:43:21.624Z\\\",\\\"eventName\\\":\\\"ObjectCreated:Copy\\\",\\\"userIdentity\\\":{\\\"principalId\\\":\\\"AWS:AIDAXVKS2VC3OL533N3PL\\\"},\\\"requestParameters\\\":{\\\"sourceIPAddress\\\":\\\"49.43.153.205\\\"},\\\"responseElements\\\":{\\\"x-amz-request-id\\\":\\\"YFXEVHJGR9NNR1FA\\\",\\\"x-amz-id-2\\\":\\\"xN5hGwyx+trhOwkHx6w8C7BIw6DlO7hJuFNzfOSWftbUdl8/CbWPlhkpPSTtfP+v7/EQOUJrTSChKLv6aiWlgybBIB2MYx91l8eOeF04d/o=\\\"},\\\"s3\\\":{\\\"s3SchemaVersion\\\":\\\"1.0\\\",\\\"configurationId\\\":\\\"sb_event\\\",\\\"bucket\\\":{\\\"name\\\":\\\"source-sb-2023\\\",\\\"ownerIdentity\\\":{\\\"principalId\\\":\\\"AV7CRGK0EWY46\\\"},\\\"arn\\\":\\\"arn:aws:s3:::source-sb-2023\\\"},\\\"object\\\":{\\\"key\\\":\\\"source_files/part-00000_orders_2.csv\\\",\\\"size\\\":4702,\\\"eTag\\\":\\\"14c73f0c4ba085969e025b0e1c7661cf\\\",\\\"sequencer\\\":\\\"0064DDCF9995930159\\\"}}}]}\",\n  \"Timestamp\" : \"2023-08-17T07:43:22.148Z\",\n  \"SignatureVersion\" : \"1\",\n  \"Signature\" : \"XGV9ZSkT/Pl/aDUG8mzUjViZrDqTM4dBKdyYUI857mT5ljKP1tQV8tSZgQqVOsI6Ox0jL6rSd2i+b3Zv0REmF4tVxP26G0lKZiO8QDmsmRVL8k9BYeIOqKXwP1sh0mqa2UIqlabBEMCyPOI36VpnknYM6i9qcbj3ciWemSCap62JiswsAuOhAU16J/nBQAiszGdp8mKVv4LCx4zMbmJflk5NkFoOE6dSQWexrx65XI/TAqvT2sOnzQfL1/7h9YcOMZlzfZH7aoE7bHMPh2l0eTQTUVkn7bk2Cchrov1t3JRuizxWIXmD+oS749xjtz5nWuxdJcwsEG6p6qoGl3AzJw==\",\n  \"SigningCertURL\" : \"https://sns.ap-south-1.amazonaws.com/SimpleNotificationService-01d088a6f77103d0fe307c0069e40ed6.pem\",\n  \"UnsubscribeURL\" : \"https://sns.ap-south-1.amazonaws.com/?Action=Unsubscribe&SubscriptionArn=arn:aws:sns:ap-south-1:526844078262:sb_topic:ae942058-0396-4673-a154-39e942f91741\"\n}",
         "attributes":{
            "ApproximateReceiveCount":"12",
            "SentTimestamp":"1692258202179",
            "SenderId":"AIDAJKTPXYYAO6CI6DPKS",
            "ApproximateFirstReceiveTimestamp":"1692258202179"
         },
         "messageAttributes":{
            
         },
         "md5OfBody":"e1c121a0d098b632c2b9a0a6850501e1",
         "eventSource":"aws:sqs",
         "eventSourceARN":"arn:aws:sqs:ap-south-1:526844078262:sb_queue",
         "awsRegion":"ap-south-1"
      }
   ]
}



body = json.loads(event['Records'][0]['body'])
message_json = json.loads(body['Message'])
bucket_name = message_json["Records"][0]["s3"]["bucket"]["name"]
object_key = message_json["Records"][0]["s3"]["object"]["key"]

print("Bucket Name:", bucket_name)
print("Object Key:", object_key)