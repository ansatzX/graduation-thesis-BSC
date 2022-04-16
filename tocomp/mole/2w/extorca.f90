!This tool was written by Dr. Tian Lu at Beijing Kein Research Center
!for Natural Sciences (www.keinsci.com)
!Contact: sobereva@sina.com

program extorca
implicit real*8 (a-h,o-z)
character*80 outname,c80,arg2,arg3
character c200tmp*200
real*8 polar(6)
real*8,allocatable :: ddip(:),hess(:,:)

call getarg(1,outname)
call getarg(2,arg2)
call getarg(3,arg3)
read(arg2,*) natm
read(arg3,*) ider !1=only force 2=also Hessian

open(11,file=outname,status="replace")

open(10,file="mol.engrad",status="old")
read(10,*)
read(10,*)
read(10,*)
read(10,*)
read(10,*)
read(10,*)
read(10,*)
read(10,*) ene
write(11,"(4D20.12)") ene,0D0,0D0,0D0
read(10,*)
read(10,*)
read(10,*)
do iatm=1,natm
        read(10,*) fx
        read(10,*) fy
        read(10,*) fz
        write(11,"(3D20.12)") fx,fy,fz
end do
close(10)

if (ider==2) then
        polar=0
        write(11,"(3D20.12)") polar
        allocate(ddip(9*natm))
        ddip=0
        write(11,"(3D20.12)") ddip

        ndim=3*natm
        allocate(hess(ndim,ndim))
        open(10,file="mol.hess",status="old")
        do while(.true.)
                read(10,"(a)") c80
                if (c80=="$hessian") exit
        end do
        read(10,*)

        ncol=5
        nt=ceiling(ndim/5D0)
        do i=1,nt !Number of frames
                ns=(i-1)*ncol+1
                if (i/=nt) ne=(i-1)*ncol+ncol
                if (i==nt) ne=ndim
                read(10,*)
                do k=1,ndim !Scan rows in each frame
                        read(10,"(a)") c200tmp
                        read(c200tmp(10:),*) hess(k,ns:ne)
                end do
        end do
        close(10)
        write(11,"(3D20.12)") ((hess(i,j),j=1,i),i=1,3*natm)
end if
close(11)
end program
