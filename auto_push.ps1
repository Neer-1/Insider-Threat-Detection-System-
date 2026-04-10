cd"C:\Users\YourName\Desktop\insider-threat-system"

# Check for changes
$status = git status --porcelain

if ($status) {
    git add .
    
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    git commit -m "Auto update: $timestamp"
    
    git push origin main
}