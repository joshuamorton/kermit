from Course import And, Or, Course


def create_courses():

    ISYE2027 = Course("ISYE2027", 3)
    ISYE2028 = Course("ISYE2028", 3)

    ECE2031 = Course("ECE2031", 2)

    MATH1551 = Course("MATH1551", 2)
    MATH1552 = Course("MATH1552", 4, And(MATH1551))
    MATH1554 = Course("MATH1554", 4)
    MATH2551 = Course("MATH2551", 2, And(MATH1552, MATH1554))
    MATH3012 = Course("MATH3012", 3, And(MATH1552, MATH1554))

    MATH3215 = Course("MATH3215", 3, And(MATH2551))
    MATH3670 = Course("MATH3670", 3, And(MATH2551))
    ISYE3770 = Course("ISYE3770", 3, And(MATH2551))

    CS1315 = Course("CS1315", 3)
    CS1371 = Course("CS1371", 3)
    CS2050 = Course("CS2050", 3)
    CS2051 = Course("CS2051", 3)
    CS1301 = Course("CS1301", 3)
    CS1331 = Course("CS1331", 3, And(Or(CS1301, CS1315, CS1371)))
    CS1332 = Course("CS1332", 3, And(CS1331))
    CS2316 = Course("CS2316", 3, And(CS1301))
    CS2110 = Course("CS2110", 4, And(CS1331))
    CS2200 = Course("CS2200", 4, And(CS2110))
    CS2261 = Course("CS2261", 4, And(CS1331))
    CS2340 = Course("CS2340", 3, And(CS1331))


    CS3510 = Course("CS3510", 3, And(Or(CS1332, MATH3012), Or(CS2050, CS2051)))
    CS3511 = Course("CS3511", 3, And(Or(CS1332, MATH3012), Or(CS2050, CS2051)))


    CS3210 = Course("CS3210", 3, And(CS2200))
    CS3220 = Course("CS3220", 3, And(CS2200))
    CS3240 = Course("CS3240", 3, And(CS2340))
    CS3251 = Course("CS3251", 3, And(CS2200))

    CS3451 = Course("CS3451", 3, And(MATH2551, Or(CS2110, CS2261), CS1332, CS2340))

    CS3600 = Course("CS3600", 3, And(CS1332))
    CS3630 = Course("CS3630", 3, And(CS1332))

    CS3651 = Course("CS3651", 4, And(ECE2031))
    CS3750 = Course("CS3750", 3)
    CS3790 = Course("CS3790", 3)
    CS4001 = Course("CS4001", 3)
    CS4002 = Course("CS4002", 3)


    CS4210 = Course("CS4210", 3, And(CS3210))
    CS4220 = Course("CS4220", 3, And(CS2200))
    CS4251 = Course("CS4251", 3, And(CS3251))
    CS4235 = Course("CS4235", 3, And(CS2200))
    CS4240 = Course("CS4240", 3, And(CS2340))
    CS4261 = Course("CS4261", 3, And(CS2200))
    CS4290 = Course("CS4290", 3, And(CS2200))
    CS4400 = Course("CS4400", 3, And(Or(CS1301, CS1315, CS1371)))
    CS4420 = Course("CS4420", 3, And(CS4400))
    CS4460 = Course("CS4460", 3, And(CS1332))
    CS4464 = Course("CS4464", 3, And(CS1331))
    CS4472 = Course("CS4472", 3)
    CS4475 = Course("CS4475", 3, And(Or(CS1301, CS1315, CS1371)))
    CS4476 = Course("CS4476", 3, And(Or(CS2110, CS2261), MATH1554))
    CS4495 = Course("CS4495", 3, And(Or(CS2110, CS2261), MATH1554))
    CS4496 = Course("CS4496", 3, And(CS3451))

    CS4510 = Course("CS4510", 3, And(Or(CS3510, CS3511), MATH3012, Or(MATH3215, MATH3670, ISYE3770, And(ISYE2028, ISYE2027))))
    CS4540 = Course("CS4540", 3, And(Or(CS3510, CS3511), MATH3012, Or(MATH3215, MATH3670, ISYE3770, And(ISYE2028, ISYE2027))))

    CS3311 = Course("CS3311", 1, And(CS2340))
    LMC3432 = Course("LMC3432", 2, None, And(CS3311))
    CS3312 = Course("CS3312", 2, And(CS3311))
    LMC3431 = Course("LMC3431", 1, And(LMC3432), And(CS3312))

