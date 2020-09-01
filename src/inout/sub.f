      subroutine multiINOUT(PLAT,PLON,N,M,QLAT,QLON,NPTS,output)
	  implicit none
	  
	  double precision PLAT(N,M),PLON(N,M), QLAT(NPTS),QLON(NPTS)
	  double precision output(N,M),WORK(4,NPTS)
      integer NPTS,N,M,i,j,GCINOUT
!f2py intent(in) :: PLAT,PLON,QLAT,QLON,NPTS,NP
!f2py intent(out):: output

	  do i = 1,N
          do j = 1,M
        output(i,j) = GCINOUT(PLAT(i,j),PLON(i,j),QLAT,QLON,NPTS,WORK)		
	  end do
          end do 
	  end subroutine
