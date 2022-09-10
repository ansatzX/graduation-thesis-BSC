program get_bond
    implicit none
    real(8) :: sum_bond
    integer(4) :: lines = 1, i, j = 0, int_atomid
    character(20) :: xtblog, atomid, headword, nuc_charge, atomsymbol
    character(32) :: output
    character(12) :: tail = ".AtomValence"
    integer(8), allocatable :: wbo(:)
    read (*, *) xtblog, lines
    
    write(output,"(1A20,1A12)") trim(xtblog), tail
    write(output,"(1A32)") adjustl(trim(output))
    write(*,"(1A32)") adjustl(output)
    allocate (wbo(lines))
    open(unit=28, file=xtblog, status="old", action="read")
    open(unit=30, file=output, status="replace", action="write")
    
    do ! find wbo block and exit
        read (28, *) headword
        !write(*,*) headword
        if (headword == "Wiberg") then
          write (30, *) "atom type wbo"
            
            do i = 1, 4,1 ! get rid of head of wbo block
              read(28,*) headword
            end do

            do i = 1, lines, 1 ! get each atom's Total Valences
                j =j +1
                do ! get one atom's Total Valences since maybe bonding with a lot atom casusing infomation printed mutil-lines
                    read (28, *) atomid
                    read(atomid,"(1I4)") int_atomid
                  
                    if ( j == int_atomid ) then ! if first word fix seq atomid, it's the right line
                        backspace (unit=28)
                        read (28, *) atomid, nuc_charge, atomsymbol, sum_bond
                        wbo(i) = NINT(sum_bond)
                        write(30,"(1I4,1A5,1I4)") j, trim(atomsymbol),wbo(i)
                        exit
                    end if

                end do
            end do
            exit

        else
            cycle
        end if
    end do

    close(28)
    close(30)
    deallocate (wbo)
end program
