# Obtener fecha para el reporte
$fecha = Get-Date -Format "ddMMyyyy"

# Ruta del reporte
$reporte = "$env:USERPROFILE\Desktop\Actividad13_reporte_$fecha.txt"

# Función para validar archivo
function Validar-Archivo {

    param ([string]$Ruta)

    try {

        if (Test-Path $Ruta) {

            $contenido = Get-Content $Ruta -ErrorAction Stop
            $mensaje = "Archivo encontrado y accesible: $Ruta"

        } 
        else {

            throw "El archivo no existe: $Ruta"

        }

    }
    catch {

        $mensaje = "Error al acceder al archivo: $_"

    }
    finally {

        Write-Host "Validación finalizada para: $Ruta" -ForegroundColor Cyan

    }

    # Mostrar en pantalla
    Write-Output $mensaje

    # Guardar en reporte
    Add-Content -Path $reporte -Value $mensaje
}

# Encabezado del reporte
Add-Content -Path $reporte -Value "REPORTE DE VALIDACIÓN DE ARCHIVOS"
Add-Content -Path $reporte -Value "Fecha: $(Get-Date)"
Add-Content -Path $reporte -Value "---------------------------------"

# Pruebas de la función

Validar-Archivo -Ruta "C:\archivo_inexistente.txt"

Validar-Archivo -Ruta "$env:USERPROFILE\Desktop\archivo.txt"