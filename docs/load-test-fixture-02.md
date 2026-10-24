# Retry Policy

The secret cache refresh runs on a fixed interval and retries on failure.

## Policy

| Attempt | Delay | Notes |
|---|---|---|
| 1 | 0 s | immediate |
| 2 | 2 s | after first failure |
| 3 | 8 s | after second failure |
| 4 | 30 s | final attempt |

The total worst-case wall clock is therefore 40 seconds, which is below the
60 second client timeout. Callers may therefore treat a refresh failure as
transient and simply retry the whole operation.

## Backoff

Backoff is multiplicative with a factor of 4. Jitter is deliberately omitted so
the behaviour is reproducible in tests. This means two processes that start at
the same moment will retry in lockstep, which is acceptable because only one
process refreshes at a time.

## Failure handling

When all four attempts fail the cache is left in its previous state and the
error is returned to the caller. The caller must not retry again, because the
underlying cause is assumed to be persistent.

## Open question

Should the final attempt be logged at warn or error level? The current code logs
at info, which means a persistent failure is invisible to alerting.
