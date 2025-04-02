# Spring Notes: 

api placeholder
https://jsonplaceholder.typicode.com/


Annotations:
- @SpringBootApplication(
scanBasePackages={"path","path2"}
 )

- @EnableAutoConfiguration
- @CompnentScan
- @Configuration

For "prototype" scoped beans, Spring does not call the destroy method. 

-@Qualifier("className")  # specify the bean id when there are multiple choices possible

ALTER TABLE student_tracker.student AUTO_INCREMENT=3000 
TURNCATE student_tracker.student //back to 1

The no-argument constructor is required by Hibernate (and JPA in general).
Who Needs It?
Hibernate (JPA Provider) → Uses reflection to instantiate entity objects when retrieving data from the database.
Spring Data JPA → When using repositories to fetch entities, it needs to create instances dynamically.


✔ JPA for API or switch DB providers easily (switch ORM providers easily), use JPA
✔ Hibernate Framework (caching, batch processing, NoSQL support), use Hibernate

Final preventions
✅ Defining constants (final int MAX_SPEED = 100;)
✅ Preventing method overriding (public final void start())
✅ Preventing class inheritance (public final class Car {})
✅ Ensuring immutable dependencies in Spring Boot (private final Engine engine;)

Docs: 
https://github.com/darbyluv2code/spring-boot-3-spring-6-hibernate-for-beginners/blob/main/11-appendix/course-links.md

# LINUX Quiz :
Please use python launcher that I did

# Git questions :
https://github.com/suyanpython/git-notes-suyan/wiki/Git-questions

# Github actions:
https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows

# Git UI tools :

https://www.sublimemerge.com/
https://fork.dev/
https://desktop.github.com/download/

# Unity
https://limezu.itch.io/
https://pipoya.itch.io/
