from . import *
### ----------------------------------
# Below are function used ONLY WHEN you first downloaded data from FinnProX
# You can opt to preprocess the data on Excel
# Note that that the code assumes specific columns are included as noted in line 72 to 113
# Note that: 'STT', 'Mã', 'Tên công ty', 'Sàn' is default columns of FiinProX raw dataset
### -----------------------------------

def prep_data(path, sheet_name='Sheet1', id_col=None, rename=True):

    '''

    :param path: path to excel file
    :param sheet_name: sheet name
    :param id_col: columns that are not melted during unpivot, default to ['Mã', 'Sàn'].
              - In case when columns, other than the two, have no year factor inside its name,
                 they must be listed alongside the two columns as followed:
                 id_col = ['Mã' , 'Sàn', Col1, ..., Col_n]
              - Example of column with year factor:
                 A. TỔNG CỘNG TÀI SẢN\nHợp nhất\nQuý: Hàng năm\nNăm: 2015\nĐơn vị: VND ==>> 2015 is year factor
              - Example of column withou year factor:
                  Số nhân viên hiện tại, Phân ngành
    :param rename: used to rename vietnamese cols -> english; ONLY USABLE WHEN the cols are same as specified
                   from line 72 -> 113
    :return: dataframe

    '''
    if id_col is None:
        id_col = ['Mã', 'Sàn']

    # Select area with relevant data
    file = pd.read_excel(path, sheet_name=sheet_name, header=7)
    idx = file[file['STT'].isna()].index.min()
    df = file[file.index < idx]

    # drop unnecessary cols
    df_unpivot = df.drop(columns=['STT', 'Tên công ty'])

    # Process
    # Unpivot table
    df_unpivot = df_unpivot.melt(id_vars=id_col, value_vars=df.columns[4:])

    # Add year cols
    df_unpivot['Year'] = df_unpivot['variable'].apply(
      lambda x: re.search(r'\d{4}', x).group()
    )
    df_unpivot['Year'] = pd.to_numeric(df_unpivot['Year'], errors='coerce')



    # clean variables column by adding 'vars_mini' column
    df_unpivot['vars_mini'] = df_unpivot['variable'].apply(
      lambda x: x.split('\n')[0]
    )
    df_unpivot['vars_mini'] = df_unpivot['vars_mini'].apply(
      lambda x: re.sub(r'\d+\.', '', x)
    )
    df_unpivot['vars_mini'] = df_unpivot['vars_mini'].apply(
      lambda x: x.strip()
    )
    # drop 'variable' column
    df_unpivot.drop(columns='variable', inplace=True)

    # pivot columns based on vars_mini
    df_final = df_unpivot.pivot(
      index=['Mã', 'Sàn', 'Year'], columns='vars_mini', values='value'
    ).reset_index()

    if rename:
        # columns rename and reposition
        df_final = df_final.rename(columns={
          'Mã': 'company',
          'Sàn': 'platform',
          'Year': 'year',

          'EBITDA': 'ebitda',

          'Doanh thu thuần': 'revenue',

          'Giá vốn hàng bán': 'cogs',
          'Chi phí bán hàng': 'sales_cost',
          'Chi phí quản lý doanh  nghiệp': 'admin_cost',

          'Lợi nhuận thuần từ hoạt động kinh doanh': 'net_op_profit',

          'Các khoản phải thu ngắn hạn': 'short_receive',
          'Hàng tồn kho, ròng': 'in_stock',
          'Giá trị ròng tài sản đầu tư': 'invest_nav',
          'Phải thu dài hạn': 'long_receive',
          'Tiền và tương đương tiền': 'cash',
          'Tài sản cố định': 'fixed_asset',
          'Tài sản dài hạn khác': 'other_long_asset',
          'Tài sản dở dang dài hạn': 'cwip',
          'Tài sản ngắn hạn khác': 'other_short_asset',
          'Đầu tư dài hạn': 'long_invest',

          'Nợ dài hạn': 'long_liability',
          'Nợ ngắn hạn': 'short_liability',

          'Vốn và các quỹ': 'equity_fund',
          'Nguồn kinh phí và quỹ khác': 'other_fund',

          'Tỷ lệ sở hữu nhà nước': 'gov_own',
          'Tỷ lệ sở hữu nước ngoài': 'for_own',

          'ROA %': 'roa',
          'ROE %': 'roe',

          'Vốn hóa thị trường': 'market_cap',
          'Giá trị doanh nghiệp (EV)': 'ev',

          'ROIC %': 'roic',
          'ROCE %': 'roce'

        })

        df_final = df_final[
          ['company', 'platform', 'year', 'ebitda', 'revenue', 'cogs', 'sales_cost', 'admin_cost', 'net_op_profit',
           'short_receive', 'in_stock', 'invest_nav', 'long_receive', 'long_liability', 'short_liability', 'cash',
           'fixed_asset',
           'other_long_asset', 'cwip', 'other_short_asset', 'long_invest', 'equity_fund', 'other_fund', 'gov_own',
           'for_own', 'roa',
           'roe', 'market_cap', 'ev', 'roic', 'roce'
           ]]

    return df_final

# Save any data as .CSV
def save_file(df_, name):
  df_.to_csv(f"{name}.csv", index=False)