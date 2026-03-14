# Obtener todos los usuarios locales del sistema
$usuarios = Get-LocalUser

# Arreglos para clasificar usuarios
$sinLogon = @()
$conLogon = @()
$deshabilitados = @()

# Recorrer cada usuario
foreach ($u in $usuarios) {

    # Verificar si el usuario está deshabilitado
    if ($u.Enabled -eq $false) {
        $deshabilitados += "$($u.Name): Usuario DESHABILITADO"
    }

    # Verificar si el usuario nunca ha iniciado sesión
    if (-not $u.LastLogon) {

        $sinLogon += "$($u.Name): Estado = $($u.Enabled), Último acceso = NUNCA"

    } else {

        $conLogon += "$($u.Name): Estado = $($u.Enabled), Último acceso = $($u.LastLogon)"

    }
}

# Guardar archivos individuales
$sinLogon | Out-File "$env:USERPROFILE\Desktop\Actividad12_usuarios_sin_logon.txt"
$conLogon | Out-File "$env:USERPROFILE\Desktop\Actividad12_usuarios_con_logon.txt"

# Crear reporte general
$reporte = @()

$reporte += "REPORTE DE AUDITORÍA DE USUARIOS"
$reporte += "Fecha: $(Get-Date)"
$reporte += "----------------------------------"
$reporte += ""

$reporte += "Usuarios que NUNCA han iniciado sesión:"
$reporte += $sinLogon
$reporte += ""

$reporte += "Usuarios que SÍ han iniciado sesión:"
$reporte += $conLogon
$reporte += ""

$reporte += "Usuarios DESHABILITADOS:"
$reporte += $deshabilitados

# Guardar reporte final
$reporte | Out-File "$env:USERPROFILE\Desktop\Actividad12_reporte_usuarios.txt"

# Mostrar resultados en pantalla
Write-Output "`nUsuarios que NUNCA han iniciado sesión:"
$sinLogon | ForEach-Object { Write-Output $_ }

Write-Output "`nUsuarios que SÍ han iniciado sesión:"
$conLogon | ForEach-Object { Write-Output $_ }

Write-Output "`nUsuarios DESHABILITADOS:"
$deshabilitados | ForEach-Object { Write-Output $_ }

Write-Output "`nReporte generado en el escritorio."