 Spring Notes: 

api placeholder
https://jsonplaceholder.typicode.com/

Powershell fast change jdk version for maven
 $env:JAVA_HOME = "C:\Program Files\Java\jdk-24"
 $env:PATH = "$env:JAVA_HOME\bin;" + $env:PATH

Annotations:
- @SpringBootApplication(
scanBasePackages={"path","path2"}
 )

Beans: 

Service Layer	@Service	Business logic

Repository Layer	@Repository	Database access

Controller Layer	@Controller	Web requests

Configuration Classes	@Bean	External libraries, manual beans

Utility Classes	@Component	Helper methods

Security	@Bean	Spring Security config

Aspect-Oriented Programming	@Aspect	Logging, monitoring

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


# React :
Try Upgrading Dependencies

npx npm-check-updates -u

npm install

npm ls request

# Images in Emails :

To avoid issues with external images being blocked, you can embed the image directly into the email using Base64 encoding. This encodes the image as a string of text and embeds it within the email itself, so there’s no need to load it from an external server.

Example of embedding an image using Base64:

<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAUA..." alt="Embedded Image">

Encourage Recipients to "Allow Images":include a view in browser link 

# LINUX Quiz :
Please use python launcher that I did

# Git questions :
https://github.com/suyanpython/git-notes-suyan/wiki/Git-questions

# Github actions:
https://docs.github.com/en/actions/writing-workflows/choosing-when-your-workflow-runs/events-that-trigger-workflows

# Quick HTTP server
npm install -g http-server
http-server

python -m http.server

# Git UI tools :
https://www.sublimemerge.com/
https://fork.dev/
https://desktop.github.com/download/

# Unity
https://limezu.itch.io/

https://pipoya.itch.io/

https://sketchfab.com/3d-models/the-hallwyl-museum-1st-floor-combined-f74eefe9f1cd4a2795a689451e723ee9

https://clara.io/library

https://www.turbosquid.com/fr/
