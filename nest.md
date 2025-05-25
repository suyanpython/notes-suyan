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
npm install --save joi


# repository 
@InjectRepository(Task) // This decorator tells NestJS to inject the Repository for the Task entity
private tasksRepository: Repository<Task>, // Declares a private property to hold the injected repository

# Built-in Methods

- tasksRepository.findOne({ where: { id } })
- tasksRepository.findOneBy({ id });
- tasksRepository.find() // find all 
- tasksRepository.save(Dto entity | entity[])
- taskLabelsRepository.create({ name: labelDto.name })
- tasksRepository.delete(task.id) = tasksRepository.delete(task)  
- update(criteria, partialEntity)
- merge(entity, plainObject): Merges a plain object into an entity.
- count(options): Counts entities.


For specific CRUD actions like save, remove, insert, update, delete, count, softDelete, merge, restore.

# Simplified Find 

- repository.findBy(where: FindOptionsWhere<Entity>): Equivalent to repository.find({ where: ... }).
- repository.findOneBy(where: FindOptionsWhere<Entity>): Equivalent to repository.findOne({ where: ... }).
- repository.findAndCountBy(where: -- 
FindOptionsWhere<Entity>): Equivalent to repository.findAndCount({ where: ... }).

They don't offer the other options like relations, select, order, skip, take, etc.

# FindManyOptions<Entity> and FindOneOptions<Entity>

FindManyOptions<Entity>: Used with repository.find() or repository.findAndCount() to retrieve multiple entities. It allows you to specify:

- where: 
- relations: Eager Loading (avoiding N+1 query problems) load in advance.
- select: 
- order:  order: { createdAt: 'DESC' }
- skip: Offset (current page) 
- take: Limit (total page)
- cache: Enables or disables query result caching.
- withDeleted: Includes soft-deleted entities if you're using @DeleteDateColumn.
- lock: Enables locking mechanisms for the query (primarily for findOne).

# FindOptionsWhere<Entity>
`const where: FindOptionsWhere<Task> = {};`

- where: { id: 1, name: 'Alice' }
- Logical OR: where: [{ name: 'Alice' }, { age: 30 }] 
- Nested Relations: where: { project: { name: 'TypeORM' } } 
TypeORM FindOperators: (for complex query)
- Not: where: { title: Not('About #1') } 
- LessThan, LessThanOrEqual: where: { likes: LessThan(10) }
- MoreThan, MoreThanOrEqual: where: { views: MoreThanOrEqual(100) }
- Like, ILike (case-insensitive Like): where: { title: Like('%keyword%') }
- Between: where: { date: Between('2023-01-01', '2023-12-31') }
- In: where: { id: In([1, 2, 3]) }
- Any: where: { tags: Any(['nest', 'typeorm']) } (for array columns)
- IsNull: where: { description: IsNull() }
- Raw: For when you need to write raw SQL within the where clause (use with caution to avoid SQL injection): where: { createdAt: Raw(alias =>${alias} > NOW() - INTERVAL '7 days') }

#Query Builder (SelectQueryBuilder, InsertQueryBuilder, UpdateQueryBuilder, DeleteQueryBuilder)

When you need fine-grained control over joins, subqueries, complex WHERE conditions, group by, having, etc.

`repository.createQueryBuilder('alias')`

- select(columns: string | string[]): Specifies columns to select.
- addSelect(columns: string | string[]): Adds more columns to select.
- from(entity: EntityTarget<Entity>, alias: string): Defines the main entity and its alias.
- where(condition: string, parameters?: ObjectLiteral): Adds a WHERE condition. You can use parameterized queries for safety.
- andWhere(condition: string, parameters?: ObjectLiteral): Adds an AND condition.
- orWhere(condition: string, parameters?: ObjectLiteral): Adds an OR condition.
- leftJoinAndSelect(relation: string, alias: string): Joins and selects columns from a related entity.
- innerJoinAndSelect(relation: string, alias: string): Similar to leftJoinAndSelect but uses an INNER JOIN.
- orderBy(sort: string, order?: 'ASC' | 'DESC', nulls?: 'NULLS FIRST' | 'NULLS LAST'): Sets the ordering.
- groupBy(column: string): Groups results.
- having(condition: string, parameters?: ObjectLiteral): Adds a HAVING condition.
- skip(offset: number): Pagination offset.
- take(limit: number): Pagination limit.
- getMany(): Executes the query and returns multiple entities.
- getOne(): Executes the query and returns a single entity.
- getManyAndCount(): Executes the query and returns both entities and their total count.
- getCount(): Returns only the count of results.
- insert().into().values(): For bulk inserts.
- update().set().where(): For bulk updates.
- delete().from().where(): For bulk deletes.


Things to take care of :
1. generics <T> , to reduce possible errors
2.  ?. optional chaining operator, it can undefined without causing a runtime error.
   ex: const prefix = this.configService.get<ConfigType>('app')?.messagePrefix;


