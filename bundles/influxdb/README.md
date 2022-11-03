# Influxdb

```bash
influx -precision rfc3339
```

```sql
CREATE DATABASE home;
```

```bash
curl -X POST http://localhost:8086/write?db=home -d 'cpu_load_short value=0.64 1590542066000000000'
```