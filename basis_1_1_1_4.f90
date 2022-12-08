module basis
  implicit none

contains
  function emsav(x,c) result(v)
    implicit none
    real,dimension(1:3)::x
    real,dimension(0:34)::c
    real::v
    ! ::::::::::::::::::::
    real,dimension(0:34)::p

    call bemsav(x,p)
    v = dot_product(p,c)

    return
  end function emsav

  subroutine bemsav(x,p)
    implicit none
    real,dimension(1:3),intent(in)::x
    real,dimension(0:34),intent(out)::p
    ! ::::::::::::::::::::
    real,dimension(0:3)::m

    call evmono(x,m)
    call evpoly(m,p)

    return
  end subroutine bemsav

  subroutine evmono(x,m)
    implicit none
    real,dimension(1:3),intent(in)::x
    real,dimension(0:3),intent(out)::m
    !::::::::::::::::::::

    m(0) = 1.0D0
    m(1) = x(3)
    m(2) = x(2)
    m(3) = x(1)

    return
  end subroutine evmono

  subroutine evpoly(m,p)
    implicit none
    real,dimension(0:3),intent(in)::m
    real,dimension(0:34),intent(out)::p
    !::::::::::::::::::::

    p(0) = m(0)
    p(1) = m(1)
    p(2) = m(2)
    p(3) = m(3)
    p(4) = p(1)*p(2)
    p(5) = p(1)*p(3)
    p(6) = p(2)*p(3)
    p(7) = p(1)*p(1)
    p(8) = p(2)*p(2)
    p(9) = p(3)*p(3)
    p(10) = p(1)*p(6)
    p(11) = p(1)*p(4)
    p(12) = p(1)*p(8)
    p(13) = p(1)*p(5)
    p(14) = p(2)*p(6)
    p(15) = p(1)*p(9)
    p(16) = p(2)*p(9)
    p(17) = p(1)*p(7)
    p(18) = p(2)*p(8)
    p(19) = p(3)*p(9)
    p(20) = p(1)*p(10)
    p(21) = p(1)*p(14)
    p(22) = p(1)*p(16)
    p(23) = p(1)*p(11)
    p(24) = p(1)*p(12)
    p(25) = p(1)*p(18)
    p(26) = p(1)*p(13)
    p(27) = p(2)*p(14)
    p(28) = p(1)*p(15)
    p(29) = p(2)*p(16)
    p(30) = p(1)*p(19)
    p(31) = p(2)*p(19)
    p(32) = p(1)*p(17)
    p(33) = p(2)*p(18)
    p(34) = p(3)*p(19)

    return
  end subroutine evpoly

end module basis
