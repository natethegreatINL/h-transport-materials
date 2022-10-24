import h_transport_materials as htm
from h_transport_materials import Diffusivity, Solubility
import h_transport_materials.conversion as c

VANADIUM_MOLAR_VOLUME = 8.34e-6  # m3/mol  https://www.aqua-calc.com/calculate/mole-to-volume-and-weight/substance/vanadium

volk_diffusivity = Diffusivity(
    D_0=2.9e-8 * htm.ureg.m**2 * htm.ureg.s**-1,
    E_D=4.2 * htm.ureg.kJ * htm.ureg.mol**-1,
    isotope="H",
    source="volkl_5_1975",
    range=(173, 573),
)

veleckis_solubility = Solubility(
    units="m-3 Pa-1/2",
    isotope="H",
    range=(519, 827),
    S_0=1.38e-1 * htm.ureg.mol * htm.ureg.m**-3 * htm.ureg.Pa**-0.5,
    E_S=-29.0 * htm.ureg.kJ * htm.ureg.mol**-1,
    source="veleckis_thermodynamic_1969",
)

schober_diffusivity = Diffusivity(
    D_0=5.6e-8 * htm.ureg.m**2 * htm.ureg.s**-1,
    E_D=9.1 * htm.ureg.kJ * htm.ureg.mol**-1,
    range=(-150 + 273.15, 200 + 273.15),
    source="schober_h_1990",
    isotope="H",
    note="found in Assessment of Database for Interaction of Tritium with ITER Plasma Facing Materials",
)  # TODO get data from experimental points, see issue #64

reiter_solubility = Solubility(
    units="m-3 Pa-1/2",
    S_0=2.1e-6
    / VANADIUM_MOLAR_VOLUME
    * htm.ureg.mol
    * htm.ureg.m**-3
    * htm.ureg.Pa**-0.5,
    E_S=-32.2 * htm.ureg.kJ * htm.ureg.mol**-1,
    source="reiter_compilation_1996",
    isotope="H",
)

properties = [volk_diffusivity, veleckis_solubility]

for prop in properties:
    prop.material = "vanadium"

htm.database += properties
