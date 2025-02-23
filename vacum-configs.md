Certainly! PostgreSQL provides a variety of configuration parameters that control the behavior of **`VACUUM`** and **`autovacuum`**. These settings allow you to fine-tune how vacuuming is performed, ensuring it meets the needs of your workload while minimizing its impact on performance.

Below is a comprehensive list of **vacuum-related configuration parameters**, along with their descriptions and default values (as of PostgreSQL 15). You can adjust these settings in the `postgresql.conf` file or via SQL commands like `ALTER SYSTEM` or `SET`.

---

### **1. General Vacuum Settings**

These settings apply to both manual `VACUUM` operations and autovacuum.

#### a. **`vacuum_cost_delay`**

- **Description**: Specifies the delay (in milliseconds) that the vacuum process will sleep after processing a certain number of pages (controlled by `vacuum_cost_limit`).
- **Default**: `0` (no delay for manual `VACUUM`, but autovacuum uses `20ms` by default).
- **Purpose**: Helps reduce the I/O impact of vacuuming by introducing pauses between operations.
- **Example**:

  ```conf
  vacuum_cost_delay = '20ms'
  ```

#### b. **`vacuum_cost_page_hit`**

- **Description**: The cost assigned to vacuuming a page found in the shared buffer cache.
- **Default**: `1`
- **Purpose**: Used to calculate the total cost of vacuuming based on the pages accessed.

#### c. **`vacuum_cost_page_miss`**

- **Description**: The cost assigned to vacuuming a page not found in the shared buffer cache (i.e., requiring disk I/O).
- **Default**: `10`
- **Purpose**: Higher cost reflects the additional overhead of reading from disk.

#### d. **`vacuum_cost_page_dirty`**

- **Description**: The cost assigned to vacuuming a page that is dirtied (modified) during the vacuum process.
- **Default**: `20`
- **Purpose**: Reflects the cost of writing modified pages back to disk.

#### e. **`vacuum_cost_limit`**

- **Description**: The accumulated cost limit before the vacuum process pauses (controlled by `vacuum_cost_delay`).
- **Default**: `200`
- **Purpose**: Controls how much work the vacuum process does before pausing to reduce I/O load.

#### f. **`vacuum_freeze_min_age`**

- **Description**: Minimum age (in transactions) at which rows are frozen during vacuuming to prevent transaction ID wraparound.
- **Default**: `50 million transactions`
- **Purpose**: Prevents old transaction IDs from causing wraparound issues.

#### g. **`vacuum_freeze_table_age`**

- **Description**: Age (in transactions) at which a table is scanned entirely to freeze old rows.
- **Default**: `150 million transactions` (or 95% of `autovacuum_freeze_max_age`).
- **Purpose**: Ensures that tables with very old rows are fully vacuumed to prevent wraparound.

#### h. **`vacuum_multixact_freeze_min_age`**

- **Description**: Minimum age (in multitransactions) at which rows are frozen during vacuuming to prevent multitransaction ID wraparound.
- **Default**: `5 million multitransactions`
- **Purpose**: Similar to `vacuum_freeze_min_age`, but for multitransactions.

#### i. **`vacuum_multixact_freeze_table_age`**

- **Description**: Age (in multitransactions) at which a table is scanned entirely to freeze old rows.
- **Default**: `150 million multitransactions` (or 95% of `autovacuum_multixact_freeze_max_age`).

---

### **2. Autovacuum-Specific Settings**

These settings control the behavior of the **autovacuum** background process, which automatically runs `VACUUM` and `ANALYZE` based on certain thresholds.

#### a. **`autovacuum`**

- **Description**: Enables or disables the autovacuum process.
- **Default**: `on`
- **Purpose**: If set to `off`, autovacuum will not run, and you must manually vacuum your database.

#### b. **`autovacuum_max_workers`**

- **Description**: Maximum number of autovacuum processes that can run concurrently.
- **Default**: `3`
- **Purpose**: Controls how many tables can be vacuumed simultaneously by autovacuum.

#### c. **`autovacuum_naptime`**

- **Description**: Time interval (in seconds) between autovacuum runs.
- **Default**: `1 minute`
- **Purpose**: Determines how frequently autovacuum checks tables for vacuuming.

#### d. **`autovacuum_vacuum_threshold`**

- **Description**: Minimum number of dead tuples before autovacuum runs on a table.
- **Default**: `50`
- **Purpose**: Prevents autovacuum from running unnecessarily on tables with few dead tuples.

#### e. **`autovacuum_vacuum_scale_factor`**

- **Description**: Fraction of the table size that must contain dead tuples before autovacuum runs.
- **Default**: `0.2` (20%)
- **Purpose**: Scales the threshold based on the size of the table.

#### f. **`autovacuum_analyze_threshold`**

- **Description**: Minimum number of rows inserted, updated, or deleted before autovacuum runs `ANALYZE` on a table.
- **Default**: `50`
- **Purpose**: Ensures that query planner statistics are updated when significant changes occur.

#### g. **`autovacuum_analyze_scale_factor`**

- **Description**: Fraction of the table size that must change before autovacuum runs `ANALYZE`.
- **Default**: `0.1` (10%)
- **Purpose**: Scales the threshold based on the size of the table.

#### h. **`autovacuum_vacuum_cost_delay`**

- **Description**: Delay (in milliseconds) that autovacuum will sleep after processing a certain number of pages.
- **Default**: `20ms`
- **Purpose**: Reduces the I/O impact of autovacuum.

#### i. **`autovacuum_vacuum_cost_limit`**

- **Description**: Accumulated cost limit before autovacuum pauses (controlled by `autovacuum_vacuum_cost_delay`).
- **Default**: `-1` (uses the value of `vacuum_cost_limit`, which defaults to `200`)
- **Purpose**: Controls how much work autovacuum does before pausing.

#### j. **`autovacuum_freeze_max_age`**

- **Description**: Maximum age (in transactions) before a table is vacuumed to prevent transaction ID wraparound.
- **Default**: `200 million transactions`
- **Purpose**: Ensures that old transaction IDs are frozen to avoid wraparound.

#### k. **`autovacuum_multixact_freeze_max_age`**

- **Description**: Maximum age (in multitransactions) before a table is vacuumed to prevent multitransaction ID wraparound.
- **Default**: `400 million multitransactions`

#### l. **`autovacuum_vacuum_insert_threshold`** (PostgreSQL 13+)

- **Description**: Minimum number of new inserts before autovacuum runs on a table.
- **Default**: `1000`
- **Purpose**: Ensures that tables with frequent inserts are vacuumed to prevent bloating.

#### m. **`autovacuum_vacuum_insert_scale_factor`** (PostgreSQL 13+)

- **Description**: Fraction of the table size that must contain new inserts before autovacuum runs.
- **Default**: `0.2` (20%)

---

### **3. Logging and Monitoring Settings**

These settings control how much information is logged about vacuum and autovacuum operations.

#### a. **`log_autovacuum_min_duration`**

- **Description**: Logs autovacuum operations that take longer than the specified duration (in milliseconds).
- **Default**: `-1` (no logging)
- **Purpose**: Helps monitor long-running autovacuum processes.

#### b. **`log_vacuum_min_duration`**

- **Description**: Logs manual `VACUUM` operations that take longer than the specified duration (in milliseconds).
- **Default**: `-1` (no logging)
- **Purpose**: Helps monitor long-running manual vacuum processes.

---

### **4. Example Configuration Adjustments**

Here’s an example of how you might adjust some of these settings for a high-write workload:

```conf
# Enable autovacuum
autovacuum = on

# Increase the number of autovacuum workers
autovacuum_max_workers = 6

# Reduce the time between autovacuum runs
autovacuum_naptime = '30s'

# Lower the thresholds for vacuuming and analyzing
autovacuum_vacuum_threshold = 1000
autovacuum_vacuum_scale_factor = 0.05
autovacuum_analyze_threshold = 1000
autovacuum_analyze_scale_factor = 0.05

# Reduce the I/O impact of autovacuum
autovacuum_vacuum_cost_delay = '10ms'
autovacuum_vacuum_cost_limit = 300

# Log long-running autovacuum operations
log_autovacuum_min_duration = '5000ms'
```

---

### **5. How to Apply Changes**

You can apply these settings in several ways:

#### a. **Edit `postgresql.conf`**

- Modify the `postgresql.conf` file directly and restart the PostgreSQL service:

  ```bash
  sudo systemctl restart postgresql
  ```

#### b. **Use `ALTER SYSTEM`**

- Use SQL commands to modify settings dynamically without editing the configuration file:

  ```sql
  ALTER SYSTEM SET autovacuum_max_workers = 6;
  SELECT pg_reload_conf();
  ```

#### c. **Set Per-Table Settings**

- Adjust settings for specific tables using `ALTER TABLE`:

  ```sql
  ALTER TABLE your_table SET (
      autovacuum_vacuum_scale_factor = 0.05,
      autovacuum_vacuum_threshold = 1000
  );
  ```

---

### **6. Summary**

PostgreSQL provides a rich set of configuration options for controlling `VACUUM` and `autovacuum`. By tuning these settings, you can ensure that vacuuming is performed efficiently and doesn't negatively impact your database's performance. Key areas to focus on include:

- **Autovacuum thresholds** (`autovacuum_vacuum_threshold`, `autovacuum_vacuum_scale_factor`)
- **Concurrency** (`autovacuum_max_workers`)
- **I/O impact** (`vacuum_cost_delay`, `vacuum_cost_limit`)
- **Transaction ID wraparound prevention** (`autovacuum_freeze_max_age`)

Let me know if you'd like help applying these settings to your specific use case!
