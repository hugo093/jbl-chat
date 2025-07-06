#!/bin/bash
set -e

sed -i -e"s/^max_connections = 100.*$/max_connections = 1000/" /pgdata-tmpfs/postgresql.conf
sed -i -e"s/^#fsync = on.*$/fsync = off/" /pgdata-tmpfs/postgresql.conf
sed -i -e"s/^#synchronous_commit = on.*$/synchronous_commit = off/" /pgdata-tmpfs/postgresql.conf
sed -i -e"s/^#full_page_writes = on.*$/full_page_writes = off/" /pgdata-tmpfs/postgresql.conf
sed -i -e"s/^#bytea_output = 'hex'.*$/bytea_output = 'escape'/" /pgdata-tmpfs/postgresql.conf
sed -i -e"s/^#log_line_prefix = ''.*$/log_line_prefix = '%m - %u - '/" /pgdata-tmpfs/postgresql.conf
