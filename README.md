<p align='center'> 
  <img src="https://capsule-render.vercel.app/api?type=waving&height=200&color=80354A&text=Actividad%20Servidores&fontColor=FFFFFF&desc=Sistemas%20Operativos%20(2026-1)&fontAlignY=30&descAlignY=54"/> 
</p>

<p align='center'>
  <img src="https://64.media.tumblr.com/a6b285a68a3ce13b94b191514634ebe2/2d4a69e4bb9eff47-1a/s1280x1920/d6e4ed08a45ceba949a27893fb109d9dbd6ba362.pnj" alt="anime image" />
</p>

<p align='center'>
  <img 
    src="https://capsule-render.vercel.app/api?type=rect&height=5&color=80354A&reversal=false&fontAlignY=40&fontColor=FFFFFF&fontSize=60"
  />
</p>


# API de ítems (ngrok)

API REST hecha con FastAPI y SQLite. Expone:
- `POST /items/` para crear uno o más ítems.
- `GET /items/` para listar todos los ítems.

El servicio se ejecuta con uvicorn usando el archivo `actividadServidores_srv.service`.  
La base de datos SQLite se llama `items.db` y se crea automáticamente al levantar la API.

Para exponer la API en internet se utiliza **ngrok**, creando un túnel HTTP hacia `http://localhost:8000`, lo que genera una URL pública que permite consumir los endpoints `/items/` desde fuera de la red local.


## Cómo encender y probar el PRIMER EJERCICIO (API + ngrok)

```bash
# ‧ 𖹭.ᐟ 1. Ir al directorio del proyecto
cd /home/mary/actividadServidores

# ‧ 𖹭.ᐟ 2. Arrancar la API
sudo systemctl restart actividadServidores_srv.service
sudo systemctl status actividadServidores_srv.service   # comprobar active (running)

# ‧ 𖹭.ᐟ 3. Probar en local
# ‧ Navegador: http://localhost:8000/items/
# ‧ Documentación: http://localhost:8000/docs

# ‧ 𖹭.ᐟ 4. Exponer la API con ngrok (solo mientras se muestra)
ngrok http 8000
# ‧ Misma ruta usando la URL pública de ngrok: https://untransferring-unprecariously-mathias.ngrok-free.dev/items/

# ‧ 𖹭.ᐟ 5. (Opcional) Apagar la API al terminar
sudo systemctl stop actividadServidores_srv.service
```


<p align='center'>
  <img 
    src="https://capsule-render.vercel.app/api?type=rect&height=5&color=80354A&reversal=false&fontAlignY=40&fontColor=FFFFFF&fontSize=60"
  />
</p>


# n8n + ngrok como servicios systemd

Este directorio contiene:

- `n8n.service`: inicia el contenedor Docker de n8n en el puerto `5678` y monta el volumen de datos.
- `ngrok-n8n.service`: abre un túnel HTTP con ngrok hacia `http://localhost:5678` para exponer n8n en una URL pública.

El comportamiento de estos servicios se ilustra en la actividad con capturas de:
- La interfaz de n8n en `http://localhost:5678`.
- El webhook `/webhook/items-n8n` accesible también por la URL pública de ngrok.


## Cómo encender y probar el SEGUNDO EJERCICIO (n8n + ngrok)

```bash
# ‧ 𖹭.ᐟ 1. Encender n8n
sudo systemctl enable n8n.service        # solo la primera vez
sudo systemctl start n8n.service
sudo systemctl status n8n.service        # comprobar active (running)

# ‧ 𖹭.ᐟ 2. Encender ngrok para n8n
sudo systemctl enable ngrok-n8n.service  # solo la primera vez
sudo systemctl start ngrok-n8n.service
sudo systemctl status ngrok-n8n.service

# ‧ 𖹭.ᐟ 3. Ver en los logs que el túnel está activo
journalctl -u ngrok-n8n.service -n 30 --no-pager

# ‧ 𖹭.ᐟ 4. Probar en el navegador
# ‧ Interfaz n8n:   http://localhost:5678
# ‧ Webhook helados: http://localhost:5678/webhook/items-n8n
# ‧ Misma ruta usando la URL pública de ngrok: https://untransferring-unprecariously-mathias.ngrok-free.dev/webhook/items-n8n

# ‧ 𖹭.ᐟ 5. Apagar servicios al terminar la demostración
sudo systemctl stop ngrok-n8n.service
sudo systemctl stop n8n.service
```

<p align='center'>
  <img 
    src="https://capsule-render.vercel.app/api?type=rect&height=5&color=80354A&reversal=false&fontAlignY=40&fontColor=FFFFFF&fontSize=60"
  />
</p>
