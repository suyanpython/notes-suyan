# Nest :
npm i g @nestjs/cli

nest new 

npm run start:dev


    │ name          │ alias       │ description                                  │
    │ application   │ application │ Generate a new application workspace         │
    │ class         │ cl          │ Generate a new class                         │
    │ configuration │ config      │ Generate a CLI configuration file            │
    │ controller    │ co          │ Generate a controller declaration            │
    │ decorator     │ d           │ Generate a custom decorator                  │
    │ filter        │ f           │ Generate a filter declaration                │
    │ gateway       │ ga          │ Generate a gateway declaration               │
    │ guard         │ gu          │ Generate a guard declaration                 │
    │ interceptor   │ itc         │ Generate an interceptor declaration          │
    │ interface     │ itf         │ Generate an interface                        │
    │ library       │ lib         │ Generate a new library within a monorepo     │
    │ middleware    │ mi          │ Generate a middleware declaration            │
    │ module        │ mo          │ Generate a module declaration                │
    │ pipe          │ pi          │ Generate a pipe declaration                  │
    │ provider      │ pr          │ Generate a provider declaration              │
    │ resolver      │ r           │ Generate a GraphQL resolver declaration      │
    │ resource      │ res         │ Generate a new CRUD resource                 │
    │ service       │ s           │ Generate a service declaration               │
    │ sub-app       │ app         │ Generate a new application within a monorepo 

    
 nest g co XXX --no-spec

npm i @nestjs/mongoose mongoose 

npm i @nestjs/config

nest generate module XXX -p common   (here we generate database and config)

npm start:dev (enter to the watching mode)


npm install class-validator class-transformer
npm install @nestjs/mapped-types

Extension for .http file: 
REST Client extension

npm i --save @nestjs/config

Things to take care of :
1. generics <T> , to reduce possible errors
2.  ?. optional chaining operator, it can undefined without causing a runtime error.
   ex: const prefix = this.configService.get<ConfigType>('app')?.messagePrefix;


