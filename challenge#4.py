a = 2
b = 3
ii = []
jj = []
kk = []
ll = []
def multiple(x,y):
    for i in range(x, y+1):
        if i%a==0 and i%b!=0:
            ii.append(i)
            count_ii = len(ii)
    print(f"Tous les nombres qui sont multiples de {a} qui ne sont pas multiples de {b} sont: {ii}, Total:{count_ii}")
    for j in range(x, y+1):
        if j%b==0 and j%a!=0:
            jj.append(j)
            count_jj = len(jj)
    print(f"Tous les nombres qui sont multiples de {b} qui ne sont pas multiples de {a} sont: {jj}, Total:{count_jj}")
    for k in range(x, y+1):
        if k%b==0 and k%a==0:
            kk.append(k)
            count_kk = len(kk)
    print(f"Dans cet intervalle, tous les nombres qui sont a la fois multiples de {a} et de {b} sont: {kk}, Total:{count_kk}")
    for l in range(x, y+1):
        if l%b!=0 and l%a!=0:
            ll.append(l)
            count_ll = len(ll)
    print(f"Tous les nombres qui ne sont ni multiples de {a} ni multiples de {b} sont: {ll}, Total:{count_ll}")

multiple(1,40)