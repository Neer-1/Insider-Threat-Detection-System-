cd"c:\Users\Neer\Desktop\litds"

# Check for changes
$status = git status --porcelain

if ($status) {
    git add .
    
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    git commit -m "Auto update: $timestamp"
    
    git push origin main
}