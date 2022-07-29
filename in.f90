! ideal comment
module my_mod
    implicit none

    private!fix
    public public_var, print_matrix  ! ideal comment

    real, parameter :: public_var = 2
    integer :: private_var
!fix
contains

    ! fix
    subroutine print_matrix(A)
        real, intent(in) :: A(:, :)!   fix

        integer :: i
        ! ideal comment
        do i = 1, size(A, 1)
            ! ideal
            print *, A(i, :)
        end do

    end subroutine print_matrix

end module my_mod

