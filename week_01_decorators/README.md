
# Week 01: Production Decorators for Backend & Application Security

A suite of production-grade Python decorators implementing essential backend patterns: Role-Based Access Control (RBAC), fault tolerance, DoS mitigation, and execution profiling.

All implementations preserve original function signatures and metadata using `functools.wraps`.

---

## Modules Overview

### 1. Access Control (`auth.py`)

* **Pattern:** Role-Based Access Control (RBAC) / Fail-Safe Defaults.
* **Purpose:** Inspects incoming caller credentials and enforces permission boundaries before function execution. Raises `PermissionError` on role mismatch, preventing broken access control vulnerabilities.
* **Key feature:** Safe dictionary access via `.get()` preventing key crashes.

### 2. Fault Tolerance (`resilience.py`)

* **Pattern:** Retry Mechanism / Network Resilience.
* **Purpose:** Intercepts transient exceptions (e.g., timeouts, connection drops) and retries the operation up to `max_attempts` with a configurable backoff delay. Transparently re-raises the exception if attempts are exhausted.
* **Key feature:** Preserves clean stack trace without swallowing critical failures.

### 3. Traffic Throttling (`rate_limiter.py`)

* **Pattern:** Sliding Window Rate Limiter.
* **Purpose:** Protects API endpoints against brute-force and DoS attacks by restricting the number of calls within a rolling time window using closure state.
* **Key feature:** In-place state mutation inside closure without leaking to global scope.

### 4. Performance Profiling (`timer.py`)

* **Pattern:** Execution Benchmarking.
* **Purpose:** Measures precise function execution time using monotonic clock (`time.perf_counter`) without polluting business logic.

---

## Technical Concepts Mastered

* Function closures and scope resolution (`LEGB` rule, mutating vs rebinding, `nonlocal`).
* Decorator factories (3-level closures for parameter injection).
* Decorator stacking order and invocation lifecycle (bottom-up wrapping, top-down execution).
* Object mutability and hashing requirements for dictionary keys.
