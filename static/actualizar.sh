while true; do
    #!/bin/bash

    # # Definir el directorio de destino en tu laptop
    # echo "$1"
    DEST_DIR="/home/bruno/Proyecto_EDA/red_ad_hoc_tesis/static/ips"
    # #DEST_DIR="/home/bruno/NUCs_vinculos/"

    # # Limpia la carpeta 'NUCs_vinculos'
    rm -r "$DEST_DIR"/*

    # Escanea la red local

    sudo arp-scan --interface=wlxd03745adf9c1 --localnet | grep -oP '(\d{1,3}\.){3}\d{1,3}' > "$DEST_DIR/laptop_ips.txt"
    # echo "fin" >> "$DEST_DIR/laptop_ips.txt"
    #Crea el archivo host.txt
    awk '{split($0, arr, "."); if (arr[4] != 21) print "nuc" arr[4] "@" $0}' $DEST_DIR/laptop_ips.txt > $DEST_DIR/hosts.txt

    tail -n +2 "$DEST_DIR/laptop_ips.txt" > "file.tmp" && mv "file.tmp" "$DEST_DIR/laptop_ips.txt"

    #Ordena a las NUCs que escaneen su entorno
    pdsh -R ssh -w ^$DEST_DIR/hosts.txt 'source ~/.bashrc && sudo arp-scan --localnet | grep -oP "(\d{1,3}\.){3}\d{1,3}" > /tmp/$USER\_ips.txt'
    echo "esperando"
    sleep 2
    echo "ya esperé"
    # Mini post-procesamiento a los archivos

    # Leer cada línea del archivo hosts.txt
    while IFS= read -r host; do
        # Extraer el ID de la NUC
        echo "laptops ip tiene esta ip en sus filas $host"
        ip=$(cut -d'.' -f4 <<< $host)
        hosts=$(echo "nuc$ip@$host")
        echo "host $hosts"
        echo "ip $ip"
        
        nucID=$(echo "$hosts" | cut -d'@' -f1)
        echo "este es el nucid $nucID"
        # Número máximo de reintentos
        MAX_RETRIES=5
        RETRY_COUNT=0
        FILE_FOUND=false
        
        # # # Intentar hasta MAX_RETRIES veces
        # while [ $RETRY_COUNT -lt $MAX_RETRIES ]; do
        #     # Verificar si el archivo existe en la NUC
        #     if ssh "$hosts" "[ -f /tmp/${nucID}_ips.txt ]"; then
        #         FILE_FOUND=true
        #         RETRY_COUNT=5
        #         echo "eswtoy aca ----"
        #     else
        #         echo "Archivo ${nucID}_ips.txt no encontrado en $hosts. Reintento $((RETRY_COUNT + 1)) de $MAX_RETRIES..."
        #         sleep 2  # Esperar 2 segundos antes de volver a intentar
        #         RETRY_COUNT=$((RETRY_COUNT + 1))
        #     fi
        # done
        
        # # Si el archivo se encuentra, realizar la transferencia
        # if $FILE_FOUND; then
        echo "Archivo encontrado. Transfiriendo ${nucID}_ips.txt desde $hosts..."
        scp "$hosts:/tmp/${nucID}_ips.txt" "$DEST_DIR"
        # else
        #     echo "Error: Archivo ${nucID}_ips.txt no disponible en $hosts después de $MAX_RETRIES intentos."
        # fi
        
    done < $DEST_DIR/laptop_ips.txt

    # # Recorrer todos los archivos .txt en el directorio
    # for file in "$DEST_DIR"/*.txt; do
    #     # Verificar que sea un archivo regular
    #     if [ -f "$file" ]; then
    #         echo "Procesando archivo: $file"
    #         # Eliminar la primera línea y sobrescribir el archivo original
    #         tail -n +2 "$file" > "$file.tmp" && mv "$file.tmp" "$file"
    #     fi
    # done


    touch "$DEST_DIR/finalizado.txt"

    echo "Post-proceso completado."
    sleep 2
done