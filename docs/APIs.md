## API and points to be noted about them:

### Document APIs:
- Single Document APIs: Index, Get, Delete and Update. Mostly we are not gonna need most of them except for Index as that is the api we are gonna use most of the time in order to index documents **one at a time**.

  [Index API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-index_.html)
  
  The basic syntax of the simplest form of index api call is as follows:
  
  `PUT twitter/tweet/1
    {
      "user" : "kimchy",
      "post_date" : "2009-11-15T14:12:12",
      "message" : "trying out Elasticsearch"
    }`
   
   The alignment is a little messed up, bear with me.
   
   The get API is really gonna be useful simply during the searching, so lets save it for that time.
   
   The delete API will delete a specific document from a specified index based on the given id
   
   [Delete API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-delete.html)
   
   The basic syntax of the simplest delete API would be:
   
   `
   DELETE /twitter/tweet/1
   `
   Deletes document of id 1 from index twitter of type tweet
   
   Then there is the [update API](https://www.elastic.co/guide/en/elasticsearch/reference/current/docs-update.html).
   
   The basic syntax of the simplest update can be done in the following way:
   
   `
   PUT test/type1/1
    {
      "counter" : 1,
      "tags" : ["red"]
    }
   `
   
   
   
   
  
