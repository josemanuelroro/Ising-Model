program testeo
use mt19937

integer :: i,j,fila,columna,ia,ja,terma,mc,npasos
integer, allocatable:: s(:,:)
integer :: seed,trial_spin,contador,nf,nr,fm,nrm,jota=1
real :: w,r,energia,magne,magnesum,enersum,du,t,tf,ts,magnesum2,enersum2
real::fil,col,eq,np,simu
character(len=50):: archivo,nombre


call system_clock(count=seed)
call sgrnd(seed)

read*,fil
read*,col
read*,t
read*,tf
read*,ts
read*,eq
read*,np
read*, simu

fila=int(fil)
columna=int(col)
terma=int(eq)
npasos=int(np)

print*,"Input Parameters"
print*,"---------------------------------------"
print*,"Rows: ", fila
print*,"Columns: ", columna
print*,"Initial Temperature: ",t
print*,"Final Temperature: ",tf
print*,"Temperature Step: ",ts
print*,"Iterations until Termalization: ",terma
print*,"MonteCarlo Iterations: ",npasos
print*,"---------------------------------------"

Allocate(s(fila,columna))
open(97,file="results.txt",status="unknown")
open(99,file="spin_f.txt",status="unknown")
open(98,file="spin.txt",status="unknown")

do i=1,fila
	read(98,*) s(i,:)
end do
close(98)



do while(t.le.tf)




contador=0
du=0
enersum=0
magnesum=0
energia=0
magne=0
magnesum2=0
enersum2=0
do mc=0,npasos


	if(mc>terma) then
		contador=contador+1
		magne=sum(s(1:fila,1:columna))/(fila*columna*1.0)
		magnesum=magnesum+magne
		magnesum2=magnesum2+magne**2

		

		do i=1,fila
			do j=1,columna
				nf=0
				nr=0
				nfm=0
				nrm=0
				if(i==1) then
					nf=i-1+fila
					end if
				if (j==1) then
					nr=j-1+columna
				end if
				if (i==fila) then
					nfm=-i
				end if
				if (j==columna) then
					nrm=-j
				end if
				energia=energia-jota*s(i,j)*(s(i-1+nf,j)+s(i+1+nfm,j)+s(i,j-1+nr)+s(i,j+1+nrm))
				
			end do
		end do
		energia=energia/(fila*columna*2)
		enersum=enersum+energia
		enersum2=enersum2+energia**2

	end if
	ia=aleatorio(1,fila)
	ja=aleatorio(1,columna)
	trial_spin=-s(ia,ja)
	nf=0
	nr=0
	nfm=0
	nrm=0
	if(ia==1) then
		nf=ia-1+fila
		end if
	if (ja==1) then
		nr=ja-1+columna
	end if
	if (ia==fila) then
		nfm=-ia
	end if
	if (ja==columna) then
		nrm=-ja
	end if

	du=-2*jota*trial_spin*(s(ia+1+nfm,ja)+s(ia,ja+1+nrm)+s(ia-1+nf,ja)+s(ia,ja-1+nr))
	if (du.le.0) then
		s(ia,ja)=trial_spin
	end if
	if (du>0) then
		w=exp(-du/t)
		r=grnd()
		if (r.le.w) then
			s(ia,ja)=trial_spin
		else
			s(ia,ja)=s(ia,ja)
		end if
	end if
	
	if (simu==1 .and. t==tf) then
		write(archivo,'(i0)') mc
		nombre="resultados\"//trim(adjustl(archivo))//".txt"
		open(96,file=trim(nombre),status="unknown")
		do i=1,fila
			write(96,*) s(i,:)
		end do
		close(96)
	end if
	
end do


write(97,*) enersum/contador,(t**-2)*(enersum2/contador-(enersum/contador)**2),&
abs(magnesum/contador),(1/t)*(magnesum2/contador-(magnesum/contador)**2),t
t=t+ts


end do

do i=1,fila
	write(99,*) s(i,:)
end do

contains

integer function aleatorio(a,b)
	integer :: a,b
	real :: r
	r=grnd()
	ja=nint((a+(b-a)*grnd()))
	return
end function

end program testeo