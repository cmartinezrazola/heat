# los ejecutables tienen su nombre __main__
# no deben tener imports relativos y deben estar fuera del package
# solo los programas que van a ser ejecutados con bat necesitan sys.path.append()
import sys
sys.path.append("C:\DATA\python")

from leafspring.predim_jb import Segments
#import Segments



#for x in Segments.Index():
#for x in Segments.Skalierungsfaktor_Federbreite():
#    print(x)
for x in zip(
          Segments.Index(),
          Segments.Y_Segment(),
          Segments.Laenge_Segment(),
          Segments.Dicke(),
          Segments.Skalierungsfaktor_Federbreite(),
          ):
    print(x)

#print("MainTabe =")
#print("y =", Segments.Y_Segment(Bereich=1, Abschnitt=1))
#print("Laenge_Segment =", Segments.Laenge_Segment(Bereich=1, Abschnitt=1))
#print("Dicke =", Segments.Dicke(Bereich=1, Abschnitt=1))
#print("Skalierungsfaktor_Federbreite =", Segments.Skalierungsfaktor_Federbreite(Bereich=1, Abschnitt=1))
#print("Federbreite =", Segments.Federbreite(Bereich=1, Abschnitt=1))
#print("Ix =", Segments.Ix(Bereich=1, Abschnitt=1))
#print("Area =", Segments.Area(Bereich=1, Abschnitt=1))
#print("Volume =", Segments.Volume(Bereich=1, Abschnitt=1))
#print("Mx1 =", Segments.Mx1(Setting=1, Last="Huben", InnereLager="ohne Steifigkeit", Bereich=1, Abschnitt=1))
#print("Qx1 =", Segments.Qx1(Setting=1, Last="Huben", InnereLager="ohne Steifigkeit", Bereich=1, Abschnitt=1))
#print("U_Biegung =", Segments.U_Biegung(Setting=1, Last="Huben", InnereLager="ohne Steifigkeit", Bereich=1, Abschnitt=1))
#print("U_Schub =", Segments.U_Schub(Setting=1, Last="Huben", InnereLager="ohne Steifigkeit", Bereich=1, Abschnitt=1))
#print("Verschiebung =", Segments.Verschiebung(Setting=1, Last="Huben", InnereLager="ohne Steifigkeit", Bereich=1, Abschnitt=1))
#print("Verdrehung =", Segments.Verdrehung(Setting=1, Last="Huben", InnereLager="ohne Steifigkeit", Bereich=1, Abschnitt=1))

#si = Segments.Index()
#print (next(si))
#print (next(si))

#for si in Segments.SEGMENT_INDEX:
#    B, A = si
#    print("Verschiebung =", si, Segments.Verschiebung(Setting=1, Last="Huben", InnereLager="ohne Steifigkeit", Bereich=B, Abschnitt=A))
   
    
