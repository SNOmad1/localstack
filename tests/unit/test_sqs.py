from localstack.services.sqs import sqs_listener
from localstack.utils.common import convert_to_printable_chars


def test_sqs_message_attrs_md5():
    msg_attrs = {
        "MessageAttribute.1.Name": "timestamp",
        "MessageAttribute.1.Value.StringValue": "1493147359900",
        "MessageAttribute.1.Value.DataType": "Number",
    }
    md5 = sqs_listener.ProxyListenerSQS.get_message_attributes_md5(msg_attrs)
    assert md5 == "235c5c510d26fb653d073faed50ae77c"


def test_convert_non_printable_chars():
    string = "invalid characters - %s %s %s" % (chr(8), chr(11), chr(12))
    result = convert_to_printable_chars(string)
    assert result == "invalid characters -   "
    result = convert_to_printable_chars({"foo": [string]})
    assert result == {"foo": ["invalid characters -   "]}

    string = "valid characters - %s %s %s %s" % (chr(9), chr(10), chr(13), chr(32))
    result = convert_to_printable_chars(string)
    assert result == string
