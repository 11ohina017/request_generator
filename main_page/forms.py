from django import forms

class RequetForm(forms.Form):

    sub_header = forms.CharField(label='サブヘッダ')
    network_number = forms.CharField(label='要求先ネットワーク番号[Hex]', max_length=2)
    pc_number = forms.CharField(label='要求先局番号[Hex]', help_text='※ ネットワークに接続されているユニットの識別番号を指定します', max_length=2)
    io_number = forms.CharField(label='要求先I/O番号[Hex]', max_length=4)
    request_length = forms.CharField(label='要求データ長[Hex]', help_text='※ これ以降の電文のバイト数(文字数)を指定します', max_length=4)
    cpu_timer = forms.CharField(label='CPUタイマ[Hex]', help_text='※ 応答待ち時間[0.25秒単位]を指定します', max_length=4)

    command_choices = [
        ('0401', '0401 (一括読出)'),
        ('0403', '0403 (ランダム読出)'),
        ('1401', '1401 (一括書込)')
    ]
    command = forms.ChoiceField(label='コマンド', help_text='※ シーケンサに対して実行するコマンドを指定します。', widget=forms.Select, choices=command_choices)

    sub_command_choices = [
        ('0000', '0000 (ワード単位)'),
        ('0001', '0001 (ビット単位)')
    ]
    sub_command = forms.ChoiceField(label='サブコマンド', help_text='※ データを取り扱う単位を指定します', widget=forms.Select, choices=sub_command_choices)

    device_code_choices = [
        ('B*', 'B* (リンクリレー)'),
        ('CC', 'CC (カウンタ・コイル)'),
        ('CN', 'CN (カウンタ・現在値)'),
        ('CS', 'CS (カウンタ・接点)'),
        ('D*', 'D* (データレジスタ/拡張データレジスタ)'),
        ('DX', 'DX (ダイレクトアクセス入力)'),
        ('DY', 'DY (ダイレクトアクセス出力)'),
        ('F*', 'F* (アナンシェータ)'),
        ('L*', 'L* (ラッチリレー)'),
        ('LCC', 'LCC (ロングカウンタ・コイル)'),
        ('LCN', 'LCN (ロングカウンタ・現在値)'),
        ('LCS', 'LCS (ロングカウンタ・接点)'),
        ('LSTC', 'LSTC (ロング積算タイマ・コイル)'),
        ('LSTN', 'LSTN (ロング積算タイマ・現在値)'),
        ('LSTS', 'LSTS (ロング積算タイマ・接点)'),
        ('LTC', 'LTC (ロングタイマ・コイル)'),
        ('LTN', 'LTN (ロングタイマ・現在値)'),
        ('LTS', 'LTS (ロングタイマ・接点)'),
        ('LZ', 'LZ (ロングインデックスレジスタ)'),
        ('M*', 'M* (内部リレー)'),
        ('R', 'R (ファイルレジスタ・ブロック切換え方式)'),
        ('RD', 'RD (リフレッシュデータレジスタ)'),
        ('SB', 'SB (リンク特殊リレー)'),
        ('SC', 'SC (積算タイマ・コイル)'),
        ('SD', 'SD (特殊レジスタ)'),
        ('SM', 'SM (特殊リレー)'),
        ('SN', 'SN (積算タイマ・現在値)'),
        ('SS', 'SS (積算タイマ・接点)'),
        ('SW', 'SW (リンク特殊レジスタ)'),
        ('TC', 'TC (タイマ・コイル)'),
        ('TN', 'TN (タイマ・現在値)'),
        ('TS', 'TS (タイマ・接点)'),
        ('V*', 'V* (エッジリレー)'),
        ('W*', 'W* (リンクレジスタ)'),
        ('X*', 'X* (入力)'),
        ('Y*', 'Y* (出力)'),
        ('Z*', 'Z* (インデックスレジスタ)'),
        ('ZR', 'ZR (ファイルレジスタ)')
    ]
    device_code = forms.ChoiceField(label='デバイスコード', help_text='※ デバイスの種類を指定します', widget=forms.Select, choices=device_code_choices)

    header_address = forms.CharField(label='メモリアドレス[Hex]', help_text='※ シーケンサのメモリのアドレスを指定します', max_length=6)
    device_point_number = forms.CharField(label='デバイス点数[Hex]', max_length=4)

    # TODO
    """
    sub_header.initial = "5000"
    network_number.initial = "00"
    pc_number.initial = "FF"
    io_number.initial = "03FF"
    request_length.initial = "0018"
    cpu_timer.initial = "0010"
    command.initial = "0401"
    sub_command.initial = "0000"
    device_code.initial = "D*"
    header_address.initial = "065535"
    device_point_number.initial = "0064"
    """
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['sub_header'].widget.attrs['class'] = 'form-control col-9'
        self.fields['sub_header'].widget.attrs['placeholder'] = '5000'

        self.fields['network_number'].widget.attrs['class'] = 'form-control col-9'
        self.fields['network_number'].widget.attrs['placeholder'] = '00'

        self.fields['pc_number'].widget.attrs['class'] = 'form-control col-9'
        self.fields['pc_number'].widget.attrs['placeholder'] = 'FF'

        self.fields['io_number'].widget.attrs['class'] = 'form-control col-9'
        self.fields['io_number'].widget.attrs['placeholder'] = '03FF'

        self.fields['request_length'].widget.attrs['class'] = 'form-control col-9'
        self.fields['request_length'].widget.attrs['placeholder'] = '0018'

        self.fields['cpu_timer'].widget.attrs['class'] = 'form-control col-9'
        self.fields['cpu_timer'].widget.attrs['placeholder'] = '0010'

        self.fields['command'].widget.attrs['class'] = 'form-control col-9'
        self.fields['command'].widget.attrs['placeholder'] = '0401'

        self.fields['sub_command'].widget.attrs['class'] = 'form-control col-9'
        self.fields['sub_command'].widget.attrs['placeholder'] = '0000'

        self.fields['device_code'].widget.attrs['class'] = 'form-control col-9'
        self.fields['device_code'].widget.attrs['placeholder'] = 'D*'

        self.fields['header_address'].widget.attrs['class'] = 'form-control col-9'
        self.fields['header_address'].widget.attrs['placeholder'] = '065535'

        self.fields['device_point_number'].widget.attrs['class'] = 'form-control col-9'
        self.fields['device_point_number'].widget.attrs['placeholder'] = '0064'

