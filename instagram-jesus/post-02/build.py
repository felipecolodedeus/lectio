import random
random.seed(7)
def torn(w,h,amp=9,step=26,top=True,bottom=True,left=True,right=True):
    pts=[]
    def j(): return random.uniform(0,amp)
    x=0
    if top:
        while x<w: pts.append((x,j())); x+=step+random.uniform(-6,6)
    else: pts+= [(0,0),(w,0)]
    pts.append((w-j() if right else w,0))
    y=0
    if right:
        while y<h: pts.append((w-j(),y)); y+=step+random.uniform(-6,6)
    else: pts.append((w,h))
    x=w
    if bottom:
        while x>0: pts.append((x,h-j())); x-=step+random.uniform(-6,6)
    else: pts.append((0,h))
    y=h
    if left:
        while y>0: pts.append((j(),y)); y-=step+random.uniform(-6,6)
    return "polygon("+",".join(f"{a:.0f}px {b:.0f}px" for a,b in pts)+")"

def folder(w,h,tabw=340,tabh=48,side='left'):
    if side=='left':
        return f"polygon(0 0,{tabw}px 0,{tabw+34}px {tabh}px,{w}px {tabh}px,{w}px {h}px,0 {h}px)"
    return f"polygon(0 {tabh}px,{w-tabw-34}px {tabh}px,{w-tabw}px 0,{w}px 0,{w}px {h}px,0 {h}px)"

T={ 'f1':folder(940,1170),'f1b':folder(940,1170,side='right'),
 'f2':folder(940,1200),'f3':folder(940,1190,side='right'),
 'f4':folder(940,1190),
 't1':torn(480,300,10,22),'t2':torn(420,120,8,18),'t3':torn(900,520,12,26),'t4':torn(980,260,10,24),
 't5':torn(900,170,9,22),'t6':torn(560,560,12,26),'t7':torn(960,350,10,24),'t8':torn(940,640,10,26),'t9':torn(1160,250,10,26),'t10':torn(460,280,9,20)}

CROSS='<svg viewBox="0 0 100 130" width="%d" height="%d"><path d="M42 4h16v34h34v16H58v72H42V54H8V38h34z" fill="%s"/></svg>'
def cross(w,fill): return CROSS%(w,int(w*1.3),fill)

html='''<!doctype html><html><head><meta charset="utf-8">
<link href="https://fonts.googleapis.com/css2?family=Anton&family=Archivo:wght@500;700;800&family=Archivo+Black&display=swap" rel="stylesheet">
<style>
*{margin:0;box-sizing:border-box}
:root{--blue:#1b3bd6;--blue2:#142a9e;--paper:#d9d9d5;--ink:#111;--cream:#ecebe4}
.s{width:1080px;height:1350px;position:relative;overflow:hidden;font-family:Archivo,sans-serif;color:var(--ink);
 background:
  radial-gradient(circle at 50% 0%,rgba(255,255,255,.12),transparent 55%),
  radial-gradient(rgba(5,10,70,.42) 1.6px,transparent 2.2px) 0 0/9px 9px,
  var(--blue)}
.s::after{content:"";position:absolute;inset:0;pointer-events:none;opacity:.28;mix-blend-mode:multiply;z-index:50;
 background:url("data:image/svg+xml;utf8,<svg xmlns='http://www.w3.org/2000/svg' width='300' height='300'><filter id='n'><feTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/><feColorMatrix values='0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 .9 0'/></filter><rect width='300' height='300' filter='url(%23n)'/></svg>")}
.abs{position:absolute}
.wrap{position:absolute;filter:drop-shadow(0 16px 20px rgba(0,0,0,.5))}
.paper{width:100%;height:100%;background:
  radial-gradient(circle at 30% 20%,rgba(255,255,255,.35),transparent 60%),var(--paper)}
.dark{background:#161616;color:#eee}
.big{font-family:"Archivo Black",sans-serif;text-transform:uppercase;line-height:.9;filter:url(#rough);letter-spacing:-3px}
.cond{font-family:Anton,Impact,sans-serif;text-transform:uppercase;line-height:1.0}
.hl{background:#111;color:#f1f1ec;padding:3px 14px;-webkit-box-decoration-break:clone;box-decoration-break:clone;line-height:1.5}
.lab{font-family:"Archivo Black",sans-serif;text-transform:uppercase;letter-spacing:1px}
.tape{position:absolute;background:rgba(232,222,178,.8);box-shadow:0 2px 4px rgba(0,0,0,.25);clip-path:polygon(0 0,4% 14%,0 28%,4% 42%,0 56%,4% 70%,0 84%,3% 100%,100% 100%,96% 84%,100% 70%,96% 56%,100% 42%,96% 28%,100% 14%,98% 0)}
.stamp{position:absolute;border:5px solid #1b3bd6;color:#1b3bd6;padding:8px 18px;font-family:"Archivo Black";text-transform:uppercase;letter-spacing:2px;mix-blend-mode:multiply;opacity:.9}
.q{font-family:"Archivo Black";text-transform:uppercase;line-height:1.12;letter-spacing:-1px}
</style></head><body>
<svg width="0" height="0" style="position:absolute"><filter id="rough"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="2" seed="4" result="t"/><feDisplacementMap in="SourceGraphic" in2="t" scale="3.2"/></filter></svg>

<!-- ============ SLIDE 1 ============ -->
<div class="s" id="s1">
 <div class="wrap" style="left:80px;top:70px;width:940px;height:1170px;transform:rotate(2.4deg)"><div class="paper" style="background:#b9bab8;clip-path:%%f1b%%"></div></div>
 <div class="wrap" style="left:60px;top:90px;width:940px;height:1170px;transform:rotate(-.6deg)"><div class="paper" style="clip-path:%%f1%%"></div></div>
 <div class="abs lab" style="left:92px;top:100px;font-size:15px;letter-spacing:2px">PERGUNTAS SOBRE JESUS</div>
 <div class="wrap" style="left:36px;top:170px;width:470px;height:260px;transform:rotate(-4deg)"><div class="dark" style="width:100%;height:100%;clip-path:%%t1%%;padding:28px 34px">
   <div style="display:flex;gap:26px;align-items:center">%%cross_w%%<div><div class="lab" style="font-size:44px;line-height:1;color:#fff">CASO<br>ABERTO</div></div></div>
   <div class="lab" style="font-size:15px;margin-top:22px;color:#aaa;letter-spacing:2px">RESPOSTA DA IGREJA CATÓLICA</div></div></div>
 <div class="abs" style="right:30px;top:330px;transform:rotate(90deg);transform-origin:right top;border:4px solid #111;padding:6px 16px;font-family:'Anton';font-size:30px;letter-spacing:2px;white-space:nowrap">SEM ENROLAÇÃO</div>
 <div class="abs big" style="left:96px;top:455px;font-size:212px;white-space:nowrap">JESUS<br>É<br>DEUS?</div>
 <div class="abs" style="left:110px;right:130px;top:1085px;text-align:center">
  <div class="lab" style="font-size:36px;border-top:5px solid var(--blue);border-bottom:5px solid var(--blue);padding:12px 0;letter-spacing:0">Já te perguntaram isso e você ficou sem resposta?</div></div>
 <div class="tape" style="left:600px;top:62px;width:200px;height:58px;transform:rotate(3deg)"></div>
</div>

<!-- ============ SLIDE 2 ============ -->
<div class="s" id="s2">
 <div class="wrap" style="left:70px;top:70px;width:940px;height:1200px;transform:rotate(-.5deg)"><div class="paper" style="clip-path:%%f2%%"></div></div>
 <div class="abs lab" style="left:104px;top:110px;font-size:17px">O QUE ELE DISSE</div>
 <div class="abs cond" style="left:104px;top:150px;width:640px;font-size:92px;color:var(--blue);line-height:.98;letter-spacing:-1px">O POVO QUE OUVIU JESUS FALAR PEGOU PEDRA.</div>
 <div class="abs" style="left:104px;right:150px;top:450px;font-size:30px;line-height:1.55;font-weight:500"><span class="hl">Gente que só dá conselho bonito não leva pedrada. Quando Jesus falava certas coisas, a reação era na hora. Eles entenderam o que Ele estava dizendo.</span></div>

 <div class="abs" style="left:104px;right:104px;top:690px">
  <div style="display:flex;gap:22px;margin-bottom:26px"><div style="width:16px;background:var(--blue);flex:none"></div><div>
   <div class="q" style="font-size:37px">“Antes que Abraão existisse, EU SOU.”</div>
   <div style="font-size:27px;line-height:1.4;margin-top:6px;font-weight:500">Jo 8,58. “Eu Sou” é o nome com que Deus se revelou a Moisés (Ex 3,14). Na hora, pegaram pedra (Jo 8,59).</div></div></div>
  <div style="display:flex;gap:22px;margin-bottom:26px"><div style="width:16px;background:var(--blue);flex:none"></div><div>
   <div class="q" style="font-size:37px">“Eu e o Pai somos um.”</div>
   <div style="font-size:27px;line-height:1.4;margin-top:6px;font-weight:500">Jo 10,30. De novo, pedras. E o motivo veio dito: “tu, sendo homem, te fazes Deus” (Jo 10,33).</div></div></div>
  <div style="display:flex;gap:22px"><div style="width:16px;background:var(--blue);flex:none"></div><div>
   <div class="q" style="font-size:37px">“Filho, os teus pecados estão perdoados.”</div>
   <div style="font-size:27px;line-height:1.4;margin-top:6px;font-weight:500">Mc 2,5-7. “Quem pode perdoar pecados, a não ser Deus?” Perguntaram certo. Jesus fez um milagre pra mostrar que tinha esse poder (Mc 2,10-11).</div></div></div>
 </div>
 <div class="wrap" style="left:690px;top:1205px;width:440px;height:280px;transform:rotate(-7deg)"><div class="dark" style="width:100%;height:100%;clip-path:%%t10%%"></div></div>
 <div class="abs" style="left:830px;top:1235px;transform:rotate(-7deg)">%%cross_sm%%</div>
 <div class="tape" style="left:90px;top:48px;width:190px;height:54px;transform:rotate(-8deg)"></div>
 <div class="stamp" style="right:100px;top:165px;font-size:30px;line-height:1.15;text-align:center;transform:rotate(7deg)">Tudo no<br>Evangelho</div>
</div>

<!-- ============ SLIDE 3 ============ -->
<div class="s" id="s3">
 <div class="wrap" style="left:70px;top:70px;width:940px;height:1190px;transform:rotate(.6deg)"><div class="paper" style="clip-path:%%f3%%"></div></div>
 <div class="abs lab" style="left:104px;top:125px;font-size:17px">E OS APÓSTOLOS?</div>
 <div class="abs big" style="left:100px;top:170px;font-size:112px;line-height:.95;letter-spacing:-2px;width:700px">TOMÉ ERA O CÉTICO DA TURMA.</div>
 <div class="abs" style="left:104px;right:150px;top:500px;font-size:30px;line-height:1.55;font-weight:500"><span class="hl">Ele falou que só acreditava se visse e tocasse as feridas. Oito dias depois, Jesus aparece e convida: “põe o dedo aqui”. E aí o cético responde (Jo 20,24-28):</span></div>
 <div class="wrap" style="left:60px;top:735px;width:960px;height:350px;transform:rotate(-2deg)"><div style="width:100%;height:100%;background:var(--blue);clip-path:%%t7%%;display:flex;align-items:center;padding:0 54px"><div class="cond" style="font-size:112px;color:#f1f1ec;line-height:.98">“MEU SENHOR E MEU DEUS!”</div></div></div>
 <div class="abs" style="left:104px;right:130px;top:1120px;font-size:29px;line-height:1.5;font-weight:700">E Jesus não corrige nem diz “calma, exagerou”. Ele aceita, e ainda abençoa quem crê sem ter visto (Jo 20,29). Esse alguém é você.</div>
 <div class="stamp" style="left:760px;top:165px;font-size:16px;line-height:1.2;text-align:center;white-space:nowrap;transform:rotate(-6deg)">Jo 1,1<br>O Verbo era Deus</div>
 <div class="tape" style="left:760px;top:55px;width:170px;height:52px;transform:rotate(10deg)"></div>
</div>

<!-- ============ SLIDE 4 ============ -->
<div class="s" id="s4">
 <div class="wrap" style="left:60px;top:80px;width:940px;height:1190px;transform:rotate(-.7deg)"><div class="paper" style="clip-path:%%f4%%"></div></div>
 <div class="abs lab" style="left:96px;top:140px;font-size:17px">A DÚVIDA MAIS COMUM</div>
 <div class="abs cond" style="left:96px;top:180px;font-size:104px;color:var(--blue);width:820px;line-height:.98">MAS COMO ASSIM, DEUS E HOMEM?</div>
 <div class="abs" style="left:96px;right:120px;top:500px;font-size:32px;line-height:1.55;font-weight:500"><span class="hl">Não é metade Deus, metade gente (CIC 464). É uma pessoa só, o Filho de Deus, que é totalmente Deus e totalmente homem, sem mistura e sem confusão. A Igreja definiu isso no Concílio de Calcedônia, em 451 (CIC 467).</span></div>
 <div class="abs" style="left:96px;right:120px;top:850px">
   <div class="lab" style="font-size:30px;margin-bottom:12px">Toda missa você reza isso:</div>
   <div class="q" style="font-size:46px;color:var(--blue)">“Deus verdadeiro de Deus verdadeiro”</div>
   <div style="font-size:26px;margin-top:6px;font-weight:500">Credo Niceno-Constantinopolitano</div>
   <div class="lab" style="font-size:30px;margin:44px 0 12px">E por que Ele fez isso?</div>
   <div style="font-size:31px;line-height:1.5;font-weight:700">Santo Atanásio resumiu: Deus se fez homem pra gente poder participar da vida de Deus (CIC 460).</div>
 </div>
 <div class="tape" style="left:480px;top:52px;width:200px;height:56px;transform:rotate(-4deg)"></div>
 <div class="wrap" style="left:690px;top:1190px;width:440px;height:280px;transform:rotate(-7deg)"><div class="dark" style="width:100%;height:100%;clip-path:%%t10%%"></div></div>
 <div class="abs" style="left:830px;top:1220px;transform:rotate(-7deg)">%%cross_sm%%</div>
 <div class="stamp" style="right:90px;top:735px;font-size:26px;line-height:1.15;text-align:center;transform:rotate(6deg)">Calcedônia<br>451</div>
</div>

<!-- ============ SLIDE 5 ============ -->
<div class="s" id="s5">
 <div class="wrap" style="left:-20px;top:60px;width:1000px;height:640px;transform:rotate(-2deg)"><div class="paper" style="clip-path:%%t8%%"></div></div>
 <div class="abs cond" style="left:60px;top:115px;font-size:96px;width:860px;line-height:1.32;transform:rotate(-2deg)">SE ELE É DEUS, NÃO DÁ PRA TRATAR COMO SÓ UM <span class="hl" style="padding:0 14px;line-height:1">PERSONAGEM</span> DA HISTÓRIA.</div>
 <div class="wrap" style="left:-40px;top:745px;width:1160px;height:250px;transform:rotate(1.5deg)"><div class="dark" style="width:100%;height:100%;clip-path:%%t9%%;display:flex;align-items:center;padding:0 90px"><div class="cond" style="font-size:96px;color:#f1f1ec;line-height:1;width:900px">DÁ PRA FALAR COM ELE HOJE.</div></div></div>
 <div class="abs" style="left:70px;right:70px;top:1050px;font-size:32px;line-height:1.5;font-weight:700;color:#fff">
  <div style="margin-bottom:14px">🔖 Salva pra ler quando a dúvida bater</div>
  <div style="margin-bottom:14px">📲 Manda pra quem diz que Ele era só um cara bom</div>
  <div>💬 Comenta a pergunta que ninguém te respondeu</div></div>
 </div>
</body></html>'''
html=html.replace('%%cross_w%%',cross(70,'#fff')).replace('%%cross_sm%%',cross(110,'#d9d9d5')).replace('%%cross_w2%%',cross(70,'#f1f1ec'))
for k,v in T.items(): html=html.replace('%%'+k+'%%',v)
open('slides.html','w').write(html)
