# About Project

## Name: MusicSurf

## Description 

This project aims to solve the problem of finding Music by it's Attributes 
like Singer, Lyricist, a word or line of lyrics.

The Learning outcome is `Information Retrieval Basics` and `Searching on Unstructured data in Natural Language`. 

## Technical Specifications

Programming Language for implementing this Project will be `Python` which is chosen due to availability 
of vast number of scientific libraries and project members are fairly familiar with it. 

This will be an WebApp which will interact with Query Engine via HTTP

#### Modules/Components of Project

**Index Builder** - This will be *core* component that will build search index from music file's attributes.

**Query Engine** - This component will take a query string and returns results after performing query on index.

**Index** - This will be created by Index Builder and Query Engine will perform queries on it. 
    It will be rebuilt/refreshed when required.

![Flow Diagrams](https://raw.githubusercontent.com/electron0zero/MusicSurf/master/docs/flow.png?token=AJEB0_zoXT04I14VAdKItS68_gPOmTGvks5YldMewA%3D%3D)

## Intended Audience

People who like to search on their music collection in Natural Language.

## Features

- Natural Language querying

- Filters
    - Singers
    - Genre
    - Year Range

- Export search results as a playlist.

## Limitations

- This Project assumes that user's music collection have complete attributes in music files.
- We are assuming that user's server computer will be capable of holding index in MainMemory. 

