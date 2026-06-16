# Part 8 — Interview Preparation

> High-yield question banks with concise, correct answers. These are the questions that actually recur in Java + Spring + DevOps interviews, organized by topic and difficulty.

[← Execution Plan](07-execution-plan.md) · [Back to README](../README.md) · [Readiness →](09-readiness-checklist.md)

> ℹ️ **About scope:** This is a **curated, high-signal set** (~200 deeply-answered questions) chosen for maximum interview ROI rather than a padded list of 450 shallow ones. Each answer is written to be *spoken aloud* in an interview. Use the [resources](03-resources.md) (Baeldung, GeeksforGeeks) to expand any area. Drill 30 min/day.

**Banks:** [Java](#-java-50) · [Spring Boot](#-spring-boot-40) · [SQL](#-sql-25) · [Microservices](#-microservices-25) · [DevOps](#-devops-25) · [AWS](#-aws-25) · [System Design](#-system-design-20)

---

## 🟦 Java (50)

### Core & OOP
1. **JDK vs JRE vs JVM?** JVM runs bytecode; JRE = JVM + standard libraries (to *run*); JDK = JRE + compiler/tools (to *develop*).
2. **`==` vs `.equals()`?** `==` compares references (or primitives by value); `.equals()` compares logical equality as defined by the class.
3. **`equals()`/`hashCode()` contract?** Equal objects must have equal hash codes; unequal objects *should* have different hash codes for performance. Break it and `HashMap`/`HashSet` misbehave.
4. **`final`, `finally`, `finalize`?** `final` = constant/non-overridable/non-extendable; `finally` = always-run block; `finalize` = deprecated GC callback (don't use).
5. **Checked vs unchecked exceptions?** Checked (`Exception`) must be declared/handled at compile time; unchecked (`RuntimeException`) need not. Use checked for recoverable conditions, unchecked for programming errors.
6. **Abstract class vs interface?** Abstract class: single inheritance, can hold state + constructors. Interface: multiple inheritance of type, default/static methods, no instance state. Prefer interfaces for capability, abstract classes for shared base.
7. **Overloading vs overriding?** Overloading = same name, different params, compile-time. Overriding = subclass redefines a method, runtime polymorphism.
8. **Why is `String` immutable?** Security, thread-safety, hashcode caching, and string pool reuse. Mutating returns a new object.
9. **`String` vs `StringBuilder` vs `StringBuffer`?** `String` immutable; `StringBuilder` mutable, not thread-safe (fast); `StringBuffer` mutable, synchronized.
10. **Pass-by-value or reference in Java?** Always pass-by-value. For objects, the *reference* is passed by value (you can mutate the object but not reassign the caller's variable).

### Collections & Generics
11. **`ArrayList` vs `LinkedList`?** ArrayList = dynamic array, O(1) random access, costly mid-inserts. LinkedList = doubly-linked, O(1) ends, O(n) access. ArrayList wins in most real cases.
12. **How does `HashMap` work?** Array of buckets indexed by `hash(key)`. Collisions chain in a linked list, converting to a balanced tree after a threshold (8) for O(log n) worst case. Resizes (doubles) at load factor 0.75.
13. **`HashMap` vs `ConcurrentHashMap`?** `HashMap` not thread-safe. `ConcurrentHashMap` uses bucket-level locking/CAS for safe concurrent access without locking the whole map.
14. **`HashMap` vs `Hashtable`?** Hashtable is legacy, fully synchronized, no null keys/values. Prefer `ConcurrentHashMap`.
15. **`fail-fast` vs `fail-safe` iterators?** Fail-fast throw `ConcurrentModificationException` on structural change (e.g., `ArrayList`); fail-safe iterate a copy (e.g., `CopyOnWriteArrayList`).
16. **`Comparable` vs `Comparator`?** `Comparable` = natural ordering (`compareTo`), one per class. `Comparator` = external/multiple orderings.
17. **What is type erasure?** Generics are compile-time only; type params are erased to their bounds (`Object`) at runtime — hence no `new T[]`, no `instanceof List<String>`.
18. **PECS?** "Producer Extends, Consumer Super": use `? extends T` when reading, `? super T` when writing.
19. **`Set` implementations difference?** `HashSet` (unordered, O(1)), `LinkedHashSet` (insertion order), `TreeSet` (sorted, O(log n)).
20. **`Iterator` vs `Iterable`?** `Iterable` is implemented by collections to return an `Iterator`, which does the actual traversal (`hasNext`/`next`).

### Streams & Functional
21. **Intermediate vs terminal operations?** Intermediate (`map`, `filter`) are lazy and return a stream; terminal (`collect`, `forEach`, `reduce`) trigger execution.
22. **`map` vs `flatMap`?** `map` 1→1 transform; `flatMap` flattens nested structures (Stream of Streams → Stream).
23. **What is `Optional` for?** Explicitly model "value may be absent" to avoid NPEs. Use `map`/`orElse`/`orElseThrow`; ⚠️ don't use it for fields/params.
24. **Are parallel streams always faster?** No. Overhead + shared-state hazards can make them slower; only help for large, CPU-bound, splittable, side-effect-free workloads.
25. **`reduce` vs `collect`?** `reduce` for immutable accumulation to a single value; `collect` for mutable reduction into containers (lists, maps).
26. **What is a functional interface?** An interface with exactly one abstract method (`@FunctionalInterface`), enabling lambdas (e.g., `Function`, `Predicate`, `Supplier`, `Consumer`).
27. **Method reference types?** Static (`Class::method`), instance of object, instance of arbitrary object, constructor (`Class::new`).

### Concurrency
28. **`Runnable` vs `Callable`?** `Callable` returns a value and can throw checked exceptions; `Runnable` returns void.
29. **What does `volatile` guarantee?** Visibility (reads see latest write) and prevents reordering for that variable — but NOT atomicity of compound actions.
30. **`synchronized` — what does it provide?** Mutual exclusion + visibility (establishes happens-before on the monitor).
31. **What is a deadlock; how to avoid?** Two threads each hold a lock the other needs. Avoid via lock ordering, tryLock with timeout, or reducing lock scope.
32. **`ReentrantLock` vs `synchronized`?** `ReentrantLock` adds tryLock, timed/interruptible lock, fairness, and condition variables — at the cost of explicit unlock in `finally`.
33. **What are `Atomic` classes?** Lock-free thread-safe operations via CAS (compare-and-swap), e.g., `AtomicInteger.incrementAndGet()`.
34. **Why prefer thread pools over `new Thread()`?** Reuse threads, bound resource usage, queueing, and lifecycle management. Use `ExecutorService`.
35. **How to size a thread pool?** CPU-bound ≈ #cores (+1); I/O-bound ≈ cores × (1 + wait/compute) — measure, don't guess.
36. **`CompletableFuture` — why?** Compose async tasks non-blockingly (`thenCompose`, `thenCombine`, `allOf`), with explicit executors and exception handling.
37. **What is the Java Memory Model (JMM)?** Defines visibility/ordering rules (happens-before) across threads, enabling safe publication and reasoning about reordering.
38. **`wait()`/`notify()` rules?** Must hold the object's monitor; `wait` releases it and suspends until `notify`/`notifyAll`. Always wait in a loop checking the condition.
39. **`ThreadLocal` use & danger?** Per-thread storage (e.g., user context). ⚠️ Leaks in thread pools if not `remove()`d.
40. **Producer-consumer in Java?** Use `BlockingQueue` (e.g., `ArrayBlockingQueue`) — `put`/`take` handle blocking and signaling for you.

### JVM, GC & Memory
41. **Heap vs stack?** Heap = objects, shared, GC-managed. Stack = per-thread frames (locals, call data), auto-freed on return.
42. **JVM memory areas?** Heap, stacks, metaspace (class metadata), PC registers, native method stack.
43. **Generational GC idea?** Most objects die young → young gen (Eden + survivors) collected often/cheaply (minor GC); survivors promoted to old gen (major GC).
44. **GC algorithms?** Serial, Parallel (throughput), G1 (balanced, default), ZGC/Shenandoah (low-pause, large heaps).
45. **Stack overflow vs OOM?** `StackOverflowError` = too-deep recursion. `OutOfMemoryError` = heap/metaspace exhausted (often a leak).
46. **What causes memory leaks in Java?** Lingering references: static collections, unclosed resources, listeners not removed, `ThreadLocal` in pools.
47. **How to diagnose a leak?** Heap dump (`jmap`/JFR) → analyze in MAT/VisualVM for dominator/retained sizes; watch GC logs for rising old gen.
48. **What is escape analysis?** JIT optimization: objects that don't "escape" a method may be stack-allocated/scalar-replaced, avoiding heap allocation.
49. **`String` interning & pool?** String literals live in a pool; `intern()` returns the pooled instance to save memory and enable `==` comparison (carefully).
50. **What is the difference between strong/soft/weak/phantom references?** Strong = never GC'd while reachable; Soft = GC'd under memory pressure (caches); Weak = GC'd at next cycle (`WeakHashMap`); Phantom = post-finalization cleanup.


---

## 🟩 Spring Boot (40)

### Core & Boot
1. **What is IoC / DI?** Inversion of Control: the container creates and wires objects. Dependency Injection supplies dependencies (constructor/setter/field) rather than objects creating them — improves testability and decoupling.
2. **Constructor vs field injection?** Prefer **constructor injection**: enables immutability (`final`), easier testing, and fails fast on missing beans. Field injection hides dependencies and complicates testing.
3. **What is a Spring Bean?** An object managed by the Spring container (created, wired, lifecycle-managed).
4. **Bean scopes?** `singleton` (default, one per container), `prototype` (new each request), plus web scopes `request`, `session`, `application`.
5. **What does `@SpringBootApplication` do?** Meta-annotation combining `@Configuration`, `@EnableAutoConfiguration`, and `@ComponentScan`.
6. **How does autoconfiguration work?** On classpath/condition detection (`@ConditionalOnClass`, etc.), Boot auto-registers sensible beans; overridable by defining your own.
7. **`@Component` vs `@Service` vs `@Repository`?** All are stereotypes for component scanning; `@Repository` adds persistence-exception translation, `@Service`/`@Component` are semantic markers.
8. **What is Spring Actuator?** Production endpoints for health, metrics, info, env, etc. — foundation for monitoring.
9. **How do profiles work?** `@Profile` + `application-{profile}.yml`; activate via `spring.profiles.active`. Used for dev/test/prod config separation.
10. **`application.properties` vs `application.yml`?** Same config, different formats; YAML is hierarchical and cleaner for nested config. Property resolution order: CLI > env > profile files > defaults.

### Web / MVC
11. **`@Controller` vs `@RestController`?** `@RestController` = `@Controller` + `@ResponseBody`, returning data (JSON) instead of view names.
12. **How does a request flow through Spring MVC?** `DispatcherServlet` → HandlerMapping → Controller → (Service) → return value → HttpMessageConverter → response.
13. **`@RequestParam` vs `@PathVariable` vs `@RequestBody`?** Query param vs URI template var vs deserialized request body.
14. **How to handle exceptions globally?** `@RestControllerAdvice` + `@ExceptionHandler` methods; return consistent error bodies (RFC 7807 `ProblemDetail`).
15. **How to validate input?** Bean Validation: `@Valid` + constraints (`@NotNull`, `@Size`), custom validators, and handle `MethodArgumentNotValidException`.
16. **What is `@Transactional` and where does it apply?** Declarative transaction boundary via AOP proxy. ⚠️ Only works on public methods called through the proxy — self-invocation bypasses it.
17. **Transaction propagation types?** `REQUIRED` (default, join/create), `REQUIRES_NEW` (suspend + new), `SUPPORTS`, `MANDATORY`, `NESTED`, etc.
18. **When does `@Transactional` roll back?** By default on unchecked exceptions/`Error`; not on checked exceptions unless `rollbackFor` is set.

### Data / JPA / Hibernate
19. **Spring Data JPA repository types?** `CrudRepository`, `PagingAndSortingRepository`, `JpaRepository`; derived query methods from method names + `@Query`.
20. **What is the N+1 problem?** Loading a list then a separate query per element's association. Fix with `JOIN FETCH`, `@EntityGraph`, or batch fetching.
21. **Lazy vs eager fetching?** Lazy loads associations on access (default for collections); eager loads immediately. Prefer lazy + explicit fetching to avoid surprises and N+1.
22. **`save()` vs `saveAndFlush()`?** `save` may defer SQL to flush time; `saveAndFlush` forces immediate flush to the DB.
23. **Entity lifecycle states?** Transient, Managed (persistent), Detached, Removed — managed by the persistence context (first-level cache).
24. **Optimistic vs pessimistic locking in JPA?** Optimistic via `@Version` (detect conflicts at commit); pessimistic via DB locks (`LockModeType.PESSIMISTIC_WRITE`).
25. **First vs second-level cache?** First-level = per-session (always on). Second-level = shared across sessions (Ehcache/Hazelcast), opt-in.

### Security
26. **Authentication vs authorization?** AuthN = who you are; AuthZ = what you're allowed to do.
27. **How does the Spring Security filter chain work?** A chain of servlet filters processes each request (auth, CSRF, authorization) before it reaches controllers.
28. **JWT vs session-based auth?** JWT = stateless, self-contained signed token, scales horizontally, hard to revoke. Sessions = server state, easy revoke, needs sticky sessions / shared store.
29. **JWT structure?** Header.Payload.Signature (base64url). Signature verifies integrity; payload holds claims (don't store secrets — it's readable).
30. **How do refresh tokens work?** Short-lived access token + long-lived refresh token; refresh exchanges for a new access token without re-login. Store/rotate refresh tokens securely.
31. **OAuth2 authorization code flow (brief)?** Client redirects user to auth server → user consents → server returns a code → client exchanges code (+secret) for tokens. Used with OIDC for login.
32. **CSRF vs CORS?** CSRF = forged authenticated request (protect with tokens, relevant for cookie auth); CORS = browser cross-origin access policy (configure allowed origins).
33. **Method-level security?** `@PreAuthorize`/`@PostAuthorize`/`@Secured` with SpEL for fine-grained authorization.

### Testing / Caching / Misc
34. **`@SpringBootTest` vs slice tests?** `@SpringBootTest` loads full context (integration); slices (`@WebMvcTest`, `@DataJpaTest`) load only relevant layers — faster, focused.
35. **Why Testcontainers?** Run real dependencies (Postgres, Kafka) in Docker for high-fidelity integration tests instead of mocks/H2.
36. **`@Mock` vs `@MockBean`?** `@Mock` (Mockito) for plain unit tests; `@MockBean` replaces a bean in the Spring context.
37. **How does `@Cacheable` work?** AOP proxy checks cache by key before invoking the method; `@CacheEvict`/`@CachePut` manage entries. ⚠️ Self-invocation bypasses it (same proxy caveat as `@Transactional`).
38. **How to schedule jobs?** `@EnableScheduling` + `@Scheduled(cron/fixedRate/fixedDelay)`; for clustered apps use ShedLock to prevent duplicate runs.
39. **Spring MVC (blocking) vs WebFlux (reactive)?** MVC = thread-per-request, simpler. WebFlux = non-blocking, event-loop, better under high-concurrency I/O; steeper learning curve.
40. **How to externalize secrets/config?** Spring Cloud Config / Vault / cloud secret managers + env vars; never commit secrets. Use `@ConfigurationProperties` for typed config.


---

## 🟪 SQL (25)

1. **Types of JOINs?** INNER (matching rows), LEFT/RIGHT OUTER (all from one side + matches), FULL OUTER (all + nulls), CROSS (Cartesian), SELF (table to itself).
2. **`WHERE` vs `HAVING`?** `WHERE` filters rows before grouping; `HAVING` filters groups after aggregation.
3. **What is an index and how does it help?** A sorted data structure (usually B-tree) enabling fast lookups/range scans, turning O(n) scans into O(log n). Speeds reads, slows writes.
4. **Clustered vs non-clustered index?** Clustered = table physically ordered by the key (one per table). Non-clustered = separate structure pointing to rows.
5. **Composite index column order — why it matters?** Index is usable left-to-right (leftmost-prefix rule). `(a,b)` helps queries on `a` or `a,b`, not `b` alone.
6. **What is a covering index?** An index containing all columns a query needs, so the engine answers from the index alone (index-only scan).
7. **How do you find a slow query's cause?** `EXPLAIN ANALYZE`: look for seq scans on large tables, bad row estimates, expensive sorts/joins; add indexes or rewrite.
8. **ACID properties?** Atomicity (all-or-nothing), Consistency (valid state transitions), Isolation (concurrent txns don't interfere), Durability (committed survives crashes).
9. **Isolation levels?** Read Uncommitted, Read Committed, Repeatable Read, Serializable — increasing isolation, decreasing concurrency.
10. **Anomalies each level prevents?** Dirty read (RU allows), non-repeatable read (RC allows), phantom read (RR may allow), all prevented at Serializable.
11. **Optimistic vs pessimistic locking?** Optimistic assumes no conflict, checks at commit (version column). Pessimistic locks rows upfront (`SELECT ... FOR UPDATE`).
12. **What is a deadlock in DB; resolution?** Two txns wait on each other's locks; the DB detects and kills one (victim). Avoid via consistent lock ordering, short txns.
13. **Normalization (1NF/2NF/3NF)?** 1NF: atomic values; 2NF: no partial dependency on part of a composite key; 3NF: no transitive dependency on non-keys. Reduces redundancy.
14. **When denormalize?** For read performance: precompute joins/aggregates, accept controlled redundancy when read-heavy and joins are costly.
15. **`DELETE` vs `TRUNCATE` vs `DROP`?** DELETE removes rows (logged, WHERE, triggers); TRUNCATE quickly empties a table (minimal logging, no WHERE); DROP removes the table entirely.
16. **`UNION` vs `UNION ALL`?** UNION removes duplicates (sort/hash cost); UNION ALL keeps all (faster).
17. **What are window functions?** Compute across a set of rows related to the current row without collapsing them (`ROW_NUMBER()`, `RANK()`, `SUM() OVER (...)`).
18. **CTE (`WITH`) — why use it?** Named, readable subqueries; supports recursion. Improves clarity for complex queries.
19. **Subquery vs JOIN?** Often equivalent; JOINs typically optimize better, but correlated subqueries or `EXISTS` can be clearer/faster for existence checks.
20. **`EXISTS` vs `IN`?** `EXISTS` short-circuits and handles NULLs better for correlated checks; `IN` fine for small static lists. Beware NULLs with `NOT IN`.
21. **Primary key vs unique key?** PK: unique + not null, one per table, identifies rows. Unique: enforces uniqueness, allows (usually one) null.
22. **What is a foreign key?** Enforces referential integrity by referencing a PK/unique key in another table.
23. **How does pagination scale; offset problem?** `LIMIT/OFFSET` degrades on large offsets (scans+discards). Use keyset/cursor pagination (`WHERE id > :last ORDER BY id`).
24. **Read replicas vs sharding?** Replicas scale reads (copies, eventual lag). Sharding splits data across nodes to scale writes/storage (adds routing/rebalancing complexity).
25. **What is MVCC?** Multi-Version Concurrency Control: readers see a consistent snapshot without blocking writers (Postgres), via row versions; `VACUUM` cleans dead tuples.

---

## 🟧 Microservices (25)

1. **Monolith vs microservices trade-offs?** Monolith: simple deploy/dev, but scaling and team autonomy suffer. Microservices: independent deploy/scale/teams, but operational + distributed-systems complexity. **Start monolith-first.**
2. **How to define service boundaries?** Around business capabilities / DDD bounded contexts; each owns its data. Avoid splitting by technical layer.
3. **Database per service — why?** Loose coupling and independent deploy/scale; shared DB creates a distributed monolith.
4. **What is an API Gateway?** Single entry point handling routing, auth, rate limiting, aggregation, TLS — keeps cross-cutting concerns out of services.
5. **Service discovery?** Services register (Eureka/Consul) so callers resolve dynamic instances; client-side or server-side load balancing.
6. **What is a circuit breaker?** Stops calling a failing dependency after a failure threshold (open state), fails fast, periodically tests recovery (half-open) — prevents cascading failures (Resilience4j).
7. **Resilience4j patterns?** Circuit breaker, retry, rate limiter, bulkhead (isolate resources), time limiter.
8. **Sync vs async communication?** REST/gRPC (sync, simple, tight coupling) vs messaging (async, decoupled, resilient, eventual consistency). Prefer async for inter-service events.
9. **Kafka core concepts?** Topics partitioned for parallelism; producers write, consumer groups read (each partition to one consumer in a group); offsets track position; ordering only within a partition.
10. **How does Kafka guarantee ordering?** Only within a partition. Use a partition key (e.g., orderId) to keep related events ordered.
11. **At-least-once vs exactly-once?** At-least-once may duplicate (need idempotent consumers); exactly-once via idempotent producer + transactions in Kafka.
12. **Consumer group rebalancing?** When members join/leave, partitions are reassigned; can cause brief processing pauses and duplicate processing near commits.
13. **Kafka vs RabbitMQ?** Kafka = distributed log, high-throughput, replayable, stream processing. RabbitMQ = traditional broker, flexible routing, per-message ack, good for task queues.
14. **What is the SAGA pattern?** Manage a distributed transaction as a sequence of local txns with compensating actions on failure. Orchestration (central coordinator) vs choreography (events).
15. **Orchestration vs choreography?** Orchestration: a coordinator directs steps (clearer, central). Choreography: services react to events (looser, harder to trace).
16. **What is the Outbox pattern?** Write business data + an event row in the same DB transaction, then a relay/CDC publishes the event — guarantees atomic state change + event (solves dual-write problem).
17. **What is CQRS?** Separate write model (commands) from read model (queries/projections), often with different stores; scales reads and simplifies complex queries. Adds eventual consistency.
18. **How to handle distributed transactions?** Avoid 2PC where possible; use SAGA + idempotency + outbox for eventual consistency.
19. **Idempotency in microservices — why & how?** Network retries cause duplicates; use idempotency keys / dedup tables / natural keys so repeated requests have one effect.
20. **Distributed tracing?** Propagate a trace ID across services (W3C traceparent); spans show latency per hop (OpenTelemetry + Jaeger/Tempo).
21. **How to centralize configuration?** Spring Cloud Config / Consul; support runtime refresh and environment separation.
22. **Strangler Fig pattern?** Incrementally replace a monolith by routing specific functions to new services until the old system is retired.
23. **How to version microservice APIs?** URI/header/media-type versioning; maintain backward compatibility and a deprecation policy; consumer-driven contract tests.
24. **What is backpressure?** Mechanism for a consumer to signal it can't keep up, preventing overload (reactive streams, bounded queues, Kafka lag handling).
25. **Common microservices anti-patterns?** Distributed monolith, shared database, chatty sync calls, no observability, premature decomposition, no resilience.

---

## 🟫 DevOps (25)

1. **What is DevOps?** Culture + practices uniting dev and ops to deliver software faster and more reliably via automation, CI/CD, and shared ownership.
2. **CI vs CD vs CD?** Continuous Integration (merge + test often), Continuous Delivery (always releasable, manual prod push), Continuous Deployment (auto to prod).
3. **What is a container?** Isolated process using namespaces (isolation) + cgroups (resource limits), sharing the host kernel — lighter than a VM.
4. **Container vs VM?** Containers share the host kernel (fast, small); VMs virtualize hardware with a full guest OS (heavier, stronger isolation).
5. **What is a Docker image vs container?** Image = immutable layered template; container = a running instance of an image.
6. **Why multi-stage Docker builds?** Build in a heavy stage, copy only artifacts into a slim runtime image — smaller, more secure images.
7. **Dockerfile best practices?** Order layers by change frequency for caching, use slim/distroless base, run as non-root, `.dockerignore`, pin versions, one process per container.
8. **What is Kubernetes?** Container orchestrator that schedules, scales, self-heals, and networks containers declaratively.
9. **Pod vs Deployment vs Service?** Pod = smallest unit (1+ containers); Deployment = manages replica sets + rolling updates; Service = stable network endpoint/load balancing.
10. **Liveness vs readiness vs startup probes?** Liveness restarts a hung container; readiness gates traffic until ready; startup protects slow-starting apps from premature liveness kills.
11. **ConfigMap vs Secret?** Both inject config; Secrets are for sensitive data (base64-encoded, not encrypted by default — use encryption at rest / external stores).
12. **How does HPA work?** Scales pod replicas based on metrics (CPU/custom) against targets; requires resource requests defined.
13. **Rolling update vs blue-green vs canary?** Rolling = gradual pod replacement; blue-green = switch traffic between two full envs; canary = route a small % to the new version, then ramp.
14. **What is Helm?** Kubernetes package manager: templated, versioned charts with values for reusable, parameterized deployments.
15. **What is Infrastructure as Code (IaC)?** Provision/manage infra via versioned declarative code (Terraform) — repeatable, reviewable, auditable.
16. **Terraform state — why does it matter?** Tracks real-world resource mapping; store remotely (S3 + locking) to enable team collaboration and prevent drift/corruption.
17. **Declarative vs imperative?** Declarative = describe desired state (Terraform, K8s manifests); imperative = step-by-step commands. Declarative is reproducible.
18. **GitOps?** Git as the single source of truth for declarative infra/apps; an agent (Argo CD/Flux) reconciles the cluster to match Git.
19. **What is a reverse proxy (Nginx)?** Fronts backends for routing, TLS termination, load balancing, caching, and security.
20. **How does TLS/HTTPS handshake work (brief)?** Negotiate cipher, server presents certificate (verified via CA chain), exchange keys, then encrypt with a symmetric session key.
21. **DNS record types?** A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), TXT, NS; TTL controls caching duration.
22. **Essential Linux troubleshooting commands?** `top/htop`, `df/du`, `free`, `netstat/ss`, `journalctl`, `ps`, `lsof`, `tail -f` on logs.
23. **What makes a good CI pipeline?** Fast feedback, runs on every push, automated tests + quality/security gates, reproducible builds, fail-fast, artifact versioning.
24. **How to manage secrets in CI/CD?** Secret stores / masked variables, short-lived OIDC tokens to cloud (no static keys), least privilege, rotation.
25. **What is observability vs monitoring?** Monitoring = predefined dashboards/alerts ("is it broken?"); observability = ability to ask new questions about system state via metrics, logs, traces ("why is it broken?").


---

## 🟨 AWS (25)

1. **What is IAM?** Identity & Access Management: users, groups, roles, and policies controlling who can do what. Follow least privilege.
2. **IAM role vs user?** User = long-lived identity with credentials; role = temporary, assumable credentials for services/cross-account (preferred — no static keys).
3. **What is an IAM policy?** JSON document granting/denying actions on resources with conditions; attached to identities or resources.
4. **EC2 instance types — how to choose?** Match workload: compute-optimized (C), memory-optimized (R/X), general (M/T burstable), storage/GPU families.
5. **EBS vs instance store vs EFS?** EBS = persistent block volume (single AZ); instance store = ephemeral local; EFS = shared elastic NFS across instances/AZs.
6. **What is S3; storage classes?** Object storage. Classes: Standard, Intelligent-Tiering, Standard-IA, One Zone-IA, Glacier/Deep Archive — trade access cost/frequency.
7. **How to secure an S3 bucket?** Block public access, bucket policies/IAM, encryption (SSE-S3/KMS), VPC endpoints, versioning, access logging.
8. **What is a VPC?** Isolated virtual network: subnets (public/private), route tables, IGW, NAT gateway, security groups, NACLs.
9. **Security group vs NACL?** SG = stateful, instance-level, allow rules only. NACL = stateless, subnet-level, allow + deny rules.
10. **Public vs private subnet?** Public has a route to an Internet Gateway; private uses a NAT gateway for outbound only — keep databases in private subnets.
11. **What is RDS; benefits?** Managed relational DB: automated backups, patching, Multi-AZ failover, read replicas, monitoring.
12. **Multi-AZ vs read replica?** Multi-AZ = synchronous standby for HA/failover (same region). Read replica = async copies to scale reads (can be cross-region).
13. **ALB vs NLB vs CLB?** ALB = L7 (HTTP, path/host routing); NLB = L4 (TCP, ultra-low latency, static IP); CLB = legacy.
14. **How does Auto Scaling work?** Scaling policies adjust instance count by metrics/schedule within min/max; integrates with ALB health checks.
15. **ECS vs EKS vs Fargate?** ECS = AWS-native orchestration; EKS = managed Kubernetes; Fargate = serverless compute for containers (no node management) under either.
16. **What is CloudWatch?** Metrics, logs, alarms, dashboards, and events for observability + automated reactions.
17. **CloudWatch vs CloudTrail?** CloudWatch = performance/operational telemetry. CloudTrail = audit log of API calls (who did what, when).
18. **What is Route53?** Managed DNS + health checks + routing policies (simple, weighted, latency, failover, geolocation).
19. **Secrets Manager vs Parameter Store?** Secrets Manager = secrets with rotation (paid); SSM Parameter Store = config + secrets (free tier, manual rotation).
20. **What is the Well-Architected Framework?** Six pillars: operational excellence, security, reliability, performance efficiency, cost optimization, sustainability.
21. **How to reduce AWS costs?** Right-size, auto-scale, spot/savings plans/reserved, S3 lifecycle policies, delete idle resources, set budgets/alarms.
22. **What is IRSA (EKS)?** IAM Roles for Service Accounts: pods assume fine-grained IAM roles via OIDC — least privilege without node-wide credentials.
23. **How to achieve high availability?** Multi-AZ deployments, auto scaling, load balancing, health checks, managed services, and decoupling via queues.
24. **What is a NAT gateway for?** Lets private-subnet resources make outbound internet calls (e.g., pulling updates) without being publicly reachable.
25. **How would you deploy a Spring Boot app on AWS?** Containerize → push to ECR → run on ECS/EKS behind an ALB; RDS for DB, ElastiCache for cache, Secrets Manager for secrets, CloudWatch for monitoring, all via Terraform.

---

## 🟥 System Design (20)

1. **How do you approach a system design question?** Clarify requirements (functional + non-functional) → estimate scale → define API + data model → high-level design → deep-dive bottlenecks → address scaling/failure/consistency → state trade-offs.
2. **Vertical vs horizontal scaling?** Vertical = bigger machine (simple, limited, single point of failure). Horizontal = more machines (scales further, needs statelessness + LB).
3. **Why design stateless services?** Any instance handles any request → easy horizontal scaling and failover. Push state to DB/cache/session store.
4. **CAP theorem?** Under a network partition you choose Consistency or Availability; you can't have both. (Partition tolerance is mandatory in distributed systems.)
5. **CP vs AP examples?** CP: prefer correctness, reject during partition (e.g., traditional RDBMS, ZooKeeper). AP: stay available, reconcile later (e.g., Cassandra, DynamoDB).
6. **What is eventual consistency?** Replicas converge to the same value given no new writes; acceptable for feeds/counts, not for bank balances.
7. **Caching strategies?** Cache-aside (lazy, app-managed), read-through, write-through (sync), write-behind (async). Choose by read/write pattern + staleness tolerance.
8. **How to handle cache invalidation?** TTL expiry, write-through/explicit eviction on update, versioned keys. ("One of the two hard problems.")
9. **What is a CDN?** Geographically distributed edge caches serving static/cacheable content close to users — reduces latency and origin load.
10. **L4 vs L7 load balancing?** L4 routes by IP/port (fast, protocol-agnostic); L7 routes by content (paths, headers) enabling smarter routing.
11. **How to scale the database?** Indexing → read replicas → caching → vertical scaling → partitioning/sharding → CQRS. Apply in that order of complexity.
12. **What is sharding; challenges?** Partition data across nodes by a shard key; challenges: hot keys, cross-shard joins/transactions, rebalancing.
13. **SQL vs NoSQL — how to choose?** SQL for relations, transactions, ad-hoc queries. NoSQL for scale, flexible schema, specific access patterns (key-value, document, wide-column, graph).
14. **Message queue vs event log?** Queue (RabbitMQ/SQS) = consume-and-delete task distribution. Log (Kafka) = retained, replayable, multiple independent consumers.
15. **How to ensure idempotency at scale?** Idempotency keys + dedup store, idempotent operations, exactly-once semantics where supported.
16. **How to design rate limiting?** Token bucket / sliding window, centralized in Redis or at the gateway, per-client keys, return 429 + Retry-After.
17. **How to handle a read-heavy system?** Caching (multi-layer), read replicas, CDN, denormalized read models, precomputation.
18. **How to handle a write-heavy system?** Sharding, async processing via queues, batching, write-optimized stores (LSM-tree DBs), buffering.
19. **How to design for high availability & fault tolerance?** Redundancy (multi-AZ), no single point of failure, health checks + failover, graceful degradation, circuit breakers, retries with backoff + jitter.
20. **What are SLI / SLO / SLA / error budget?** SLI = measured metric (e.g., latency). SLO = internal target. SLA = external contract + penalties. Error budget = allowed unreliability (1 − SLO) that governs release risk.

---

## 🎯 Behavioral & Senior-Signal Questions (bonus)

Senior interviews weigh these heavily. Prepare STAR-format stories for:
- A production incident you diagnosed and fixed (and what you changed afterward).
- A technical decision with trade-offs you drove and how you aligned others.
- A time you mentored someone or improved team process.
- A disagreement on design and how you resolved it with data.
- A project that failed/slipped and what you learned.

> ✅ **Interview Checkpoint:** You can answer any question above aloud in <2 minutes, and walk through 3+ system designs and your ShopSphere project end-to-end.

[← Execution Plan](07-execution-plan.md) · [Back to README](../README.md) · [Readiness →](09-readiness-checklist.md)
