# Nombre de la app y del stack (todo bajo tu apellido)
APP_NAME=cadena
STACK_NAME=cadena
STACK_FILE=stack.yml

# Imagen que empuja el pipeline CI/CD
IMAGE=ghcr.io/matth23-sys/cadena-app:1.0.5

# Construir imagen local
build:
	docker build -t $(APP_NAME):latest .

# Desplegar stack en Swarm
deploy:
	docker stack deploy --with-registry-auth -c $(STACK_FILE) $(STACK_NAME)

# Ver logs del servicio
logs:
	docker service logs -f $(STACK_NAME)_$(APP_NAME)

# Remover stack
rm:
	docker stack rm $(STACK_NAME)

# Lista servicios activos
ps:
	docker service ls

# Reiniciar servicio completamente
restart:
	make rm
	sleep 5
	make build
	make deploy
