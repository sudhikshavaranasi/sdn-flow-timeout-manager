# SDN Flow Rule Timeout Manager

## Problem Statement

This project implements a Software Defined Networking (SDN) solution using Mininet and POX controller. The goal is to demonstrate dynamic network behavior using controller-based flow management.

## Objectives

* Demonstrate controller-switch interaction
* Implement dynamic traffic control (allow/block)
* Observe network behavior changes

## Setup & Execution

### 1. Start POX Controller

```bash
cd pox
./pox.py forwarding.timeout_controller
```

### 2. Start Mininet

```bash
sudo mn --controller=remote,ip=127.0.0.1
```

### 3. Test

```bash
h1 ping h2
```

## Expected Output

* Traffic alternates between:

  * Allowed (successful ping)
  * Blocked (packet loss / unreachable)
* Behavior changes every few seconds

## Test Scenarios

1. Allowed vs Blocked traffic
2. Dynamic switching behavior

## Proof of Execution

* Ping results showing success and failure
* Controller logs (Allowing / Blocking)
* Flow table outputs (ovs-ofctl dump-flows)

## Conclusion

This project demonstrates how SDN controllers can dynamically manage network behavior using flow rules and centralized control.
