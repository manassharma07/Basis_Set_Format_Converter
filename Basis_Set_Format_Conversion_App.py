import streamlit as st
import basis_set_exchange as bse
import os
# Set page config
st.set_page_config(page_title='Basis Set Converter', layout='wide', page_icon="🧊",
menu_items={
         'About': "# This online tool allows you to enter a basis set (and ECPs) in the form of text input for a variety of Quantum Chemistry softwares, and convert it to another format."
     })

# Sidebar stuff
st.sidebar.write('# About')
st.sidebar.write('### Made By [Manas Sharma](http://manas.bragitoff.com/)')
st.sidebar.write('### in the group of [Prof. Dr. Marek Sierka](https://www.cmsg.uni-jena.de/)')
st.sidebar.write('### for the [TURBOMOLE](https://www.turbomole.org/) program package')
st.sidebar.write('### *Powered by [Basis Set Exchange](https://github.com/MolSSI-BSE/basis_set_exchange)*')
st.sidebar.write('Basis Set Exchange (BSE) is a repository for quantum chemistry basis sets, which also provides a flexible and powerful API to facilitate reading/writing or converting basis sets.')
st.sidebar.write('[API Documentation for BSE](https://molssi-bse.github.io/basis_set_exchange/index.html)')
st.sidebar.write('The BSE library is available under the [BSD 3-Clause license](https://github.com/MolSSI-BSE/basis_set_exchange/blob/master/LICENSE)')
st.sidebar.write("For some reason, the master branch of BSE on GitHub doesn't have readers/writers available for the `crystal` basis set format. ")
st.sidebar.write('Fortunately, there is a branch by [Susi Lehtola](https://github.com/susilehtola) available [here](https://github.com/susilehtola/basis_set_exchange/tree/crystal) which provides support for `crystal` format.')
st.sidebar.write('This online tool uses that particular branch.')

# Main app
st.write('# Basis Set Format Converter')
st.write('This online tool allows you to enter a basis set in the form of text input for a variety of Quantum Chemistry softwares, and convert it to another format.')


placeholder_basis_str = '''# Example input: def2-SVP basis for Carbon in Turbomole format
$basis
*
c def2-SVP
*
   5  s
  1238.4016938      .54568832082E-02
  186.29004992      .40638409211E-01
  42.251176346      .18025593888
  11.676557932      .46315121755
  3.5930506482      .44087173314
   1  s
  .40245147363      1.0000000000
   1  s
  .13090182668      1.0000000000
   3  p
  9.4680970621      .38387871728E-01
  2.0103545142      .21117025112
  .54771004707      .51328172114
   1  p
  .15268613795      1.0000000000
   1  d
  .80   1.00
*
# K. Eichkorn, F. Weigend, O. Treutler, R. Ahlrichs; Theor. Chem. Acc. 97, 119 (1997).
$end
'''
col1, col2 = st.columns(2)
col1.write('## INPUT')
input_format = col1.selectbox('Select the input basis set format',
     ( 'turbomole', 'crystal', 'gaussian94', 'nwchem', 'dalton','molcas','cfour','genbas','gbasis','demon2k','ricdlib'))
input_basis_str = col1.text_area(label='Enter your own Basis Set here', value = placeholder_basis_str, placeholder = 'Put your text here', height=400)
# Get rid of empty lines
input_basis_str = os.linesep.join([s for s in input_basis_str.splitlines() if s])




col2.write('## OUTPUT')
output_format = col2.selectbox('Select the output basis set format',
     ( 'crystal', 'turbomole', 'gaussian94', 'nwchem', 'dalton','molcas','cfour','genbas','gbasis','demon2k','ricdlib','psi4','qchem','orca','cp2k','gamess_us','gamess_uk','pqs','molpro','cfour','xtron','acesii'))
# Parse the processed list of basis set lines (use .splitlines)
# basis_read_from_crystal_format = bse.readers.crystal.read_crystal(input_basis_str.splitlines())
# BSE JSON Format
basis_dict_bse = bse.readers.read.read_formatted_basis_str(input_basis_str, basis_fmt=input_format)
output_basis_str = bse.writers.write.write_formatted_basis_str(basis_dict_bse, fmt=output_format)
col2.text_area(label='Converted basis set in the format selected by you',value=output_basis_str, height=400)


st.write('## Basis Set Exchange JSON Format')
st.write('For debugging')
st.write(basis_dict_bse)