from django import forms

class RequetForm(forms.Form):

    sub_header = forms.CharField(label='サブヘッダ', max_length=4)
    network_number = forms.CharField(label='要求先ネットワーク番号', max_length=2)
    pc_number = forms.CharField(label='要求先局番号', max_length=2)
    """"
    io_number = forms.CharField(label='要求先I/O番号', max_length=4)
    request_length = forms.CharField(label='要求データ長', max_length=4)
    cpu_timer = forms.CharField(label='CPUタイマ', max_length=4)
    command = forms.CharField(label='コマンド', max_length=4)
    sub_command = forms.CharField(label='サブコマンド', max_length=4)
    device_code = forms.CharField(label='デバイスコード', max_length=4)
    header_address = forms.CharField(label='先頭アドレス', max_length=6)
    device_point_number = forms.CharField(label='デバイス点数', max_length=4)
"""
    #    message = forms.CharField(label='メッセージ', widget=forms.Textarea)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['sub_header'].widget.attrs['class'] = 'form-control col-9'
        self.fields['sub_header'].widget.attrs['placeholder'] = '5000'

        self.fields['network_number'].widget.attrs['class'] = 'form-control col-9'
        self.fields['network_number'].widget.attrs['placeholder'] = '00'

        self.fields['pc_number'].widget.attrs['class'] = 'form-control col-9'
        self.fields['pc_number'].widget.attrs['placeholder'] = 'FF'

        """
        self.fields['io_number'].widget.attrs['class'] = 'form-control col-9'
        self.fields['io_number'].widget.attrs['placeholder'] = '00'

        self.fields['request_length'].widget.attrs['class'] = 'form-control col-9'
        self.fields['request_length'].widget.attrs['placeholder'] = '0018'

        self.fields['cpu_timer'].widget.attrs['class'] = 'form-control col-9'
        self.fields['cpu_timer'].widget.attrs['placeholder'] = '0010'

        self.fields['command'].widget.attrs['class'] = 'form-control col-9'
        self.fields['command'].widget.attrs['placeholder'] = '0401'

        self.fields['sub_command'].widget.attrs['class'] = 'form-control col-9'
        self.fields['sub_command'].widget.attrs['placeholder'] = '0000'
For
        self.fields['device_code'].widget.attrs['class'] = 'form-control col-9'
        self.fields['device_code'].widget.attrs['placeholder'] = 'D*'

        self.fields['header_address'].widget.attrs['class'] = 'form-control col-9'
        self.fields['header_address'].widget.attrs['placeholder'] = '000100'

        self.fields['device_point_number'].widget.attrs['class'] = 'form-control col-9'
        self.fields['device_point_number'].widget.attrs['placeholder'] = '000B'
        """
    def generate_request(self):

        #name = self.cleaned_data['sub_header']
        name = "name"
        return name