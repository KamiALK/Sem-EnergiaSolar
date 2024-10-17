
# Configurar GitHub con claves SSH

Para usar GitHub desde la consola con autenticación mediante claves, sigue estos pasos:

## 1. Generar una clave SSH

Si no tienes una clave SSH generada en tu máquina, crea una con el siguiente comando:

```bash
ssh-keygen -t ed25519 -C "tu_correo@ejemplo.com"

```

o este si sale error

```bash
ssh-keygen -t rsa -b 4096 -C "tu_correo@ejemplo.com"

```

2. Agregar tu clave SSH al agente

Ejecuta los siguientes comandos para agregar la clave SSH generada al agente SSH:

```bash
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```

# Agregar  claves SSH a GitHub

## 1.  copear la clave SSH

```bash
cat ~/.ssh/id_ed25519.pub
```

# 4. Clonar repositorios usando SSH

Cuando clones un repositorio, usa la URL SSH en lugar de la URL HTTPS:

```bash
git git@github.com:KamiALK/Sem-EnergiaSolar.git
```
