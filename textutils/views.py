#i made this file.

from django.http import HttpResponse
from django.shortcuts import render

#model for Trail page
def home(request):
      return render(request,'Trail.html')

#model for Analyz page
def analyz(request):
      at = request.POST.get('text')
      rp = request.POST.get('removepunc','off')
      uc = request.POST.get('uppercase','off')
      cc = request.POST.get('character','off')

      if rp == "on":
            if uc == "on":
                  if cc == "on":
                        panctuations = ''' ’'()[]{}<>:,‒–—―…!.«»-‐?‘’“”";/⁄␠·&"@*\•^¤¢$€£¥₩₪†‡°¡¿¬#№%‰‱¶′§~¨_|⁂☞∴‽※ '''
                        analyzed = ""
                        for char in at:
                              if char not in panctuations:
                                    analyzed= analyzed + char
                        rpuc = analyzed.upper()
                        capital = rpuc
                        cccc = len(rpuc)
                        params = {"purpose": "remove punctuations and make count and uppercase.", "at": capital, "ccc": cccc}
                        return render(request, 'Analyz_mark3.html', params)
                  else:
                        panctuations = ''' ’'()[]{}<>:,‒–—―…!.«»-‐?‘’“”";/⁄␠·&"@*\•^¤¢$€£¥₩₪†‡°¡¿¬#№%‰‱¶′§~¨_|⁂☞∴‽※ '''
                        analyzed = ""
                        for char in at:
                              if char not in panctuations:
                                    analyzed = analyzed + char
                        rpuc = analyzed.upper()
                        params = {"purpose": "remove punctuations and make Uppercase.", "at": rpuc}
                        return render(request, 'Analyz.html', params)
            elif cc == "on":
                  panctuations = ''' ’'()[]{}<>:,‒–—―…!.«»-‐?‘’“”";/⁄␠·&"@*\•^¤¢$€£¥₩₪†‡°¡¿¬#№%‰‱¶′§~¨_|⁂☞∴‽※ '''
                  analyzed = ""
                  for char in at:
                        if char not in panctuations:
                              analyzed = analyzed + char
                  rpcc = len(analyzed)
                  params = {"purpose": "counter and rp.", "at": analyzed, "ccc": rpcc}
                  return render(request, 'Analyz_mark3.html', params)
            else:
                  panctuations = ''' ’'()[]{}<>:,‒–—―…!.«»-‐?‘’“”";/⁄␠·&"@*\•^¤¢$€£¥₩₪†‡°¡¿¬#№%‰‱¶′§~¨_|⁂☞∴‽※ '''
                  analyzed = ""
                  for char in at:
                        if char not in panctuations:
                              analyzed = analyzed + char
                  params = {"purpose":"Remove punctuations.","at":analyzed}
                  return render(request,'Analyz.html',params)
      elif uc == "on":
            if cc == "on":
                  analyzed = at.upper()
                  count = len(analyzed)
                  params = {"purpose": "Uppercase and caracter count.", "at":analyzed ,"ccc":count}
                  return render(request, 'Analyz_mark3.html', params)
            else:
                  analyzed = at.upper()
                  params = {"purpose": "uppercase.", "at": analyzed}
                  return render(request, 'Analyz.html', params)

      elif cc == "on":
            analyzed = len(at)
            params = {"purpose": "uppercase.", "at": analyzed}
            return render(request, 'Analyz.html', params)

      else:
            params = {"purpose": "Normal text.", "at": at}
            return render(request, 'Analyz.html', params)
