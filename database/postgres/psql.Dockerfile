# Use the official PostgreSQL client image from Docker Hub
FROM postgres:latest

# Install psql client package
# RUN apt-get update && apt-get install -y postgresql-client
RUN echo '#!/bin/bash' > run_psql.sh
RUN echo '' >> run_psql.sh
RUN echo '# Run psql command' >> run_psql.sh
RUN echo 'psql -h postgres -U tefos -d tmdb' >> run_psql.sh

RUN chmod +x run_psql.sh
# ENTRYPOINT ["/bin/bash", "-c"]
ENTRYPOINT ["/bin/bash"]

# CMD [ "psql","-h postgres -p 5432 -U tefos -d tmdb" ]
