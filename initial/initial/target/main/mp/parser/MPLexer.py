# Generated from main/mp/parser/MP.g4 by ANTLR 4.7.1
from antlr4 import *
from io import StringIO
from typing.io import TextIO
import sys


from lexererr import *


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2:")
        buf.write("\u022d\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\4.")
        buf.write("\t.\4/\t/\4\60\t\60\4\61\t\61\4\62\t\62\4\63\t\63\4\64")
        buf.write("\t\64\4\65\t\65\4\66\t\66\4\67\t\67\48\t8\49\t9\4:\t:")
        buf.write("\4;\t;\4<\t<\4=\t=\4>\t>\4?\t?\4@\t@\4A\tA\4B\tB\4C\t")
        buf.write("C\4D\tD\4E\tE\4F\tF\4G\tG\4H\tH\4I\tI\4J\tJ\4K\tK\4L\t")
        buf.write("L\4M\tM\4N\tN\4O\tO\4P\tP\4Q\tQ\4R\tR\4S\tS\4T\tT\4U\t")
        buf.write("U\4V\tV\4W\tW\3\2\3\2\3\2\3\2\7\2\u00b4\n\2\f\2\16\2\u00b7")
        buf.write("\13\2\3\2\3\2\3\2\3\2\3\2\3\3\3\3\7\3\u00c0\n\3\f\3\16")
        buf.write("\3\u00c3\13\3\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\7\4\u00cd")
        buf.write("\n\4\f\4\16\4\u00d0\13\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3")
        buf.write("\5\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\6\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3")
        buf.write("\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r")
        buf.write("\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\17\3\17\3\17\3\17")
        buf.write("\3\17\3\17\3\20\3\20\3\20\3\20\3\20\3\20\3\21\3\21\3\21")
        buf.write("\3\21\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\22\3\23")
        buf.write("\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\23\3\24\3\24")
        buf.write("\3\24\3\24\3\25\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\31\3\31\3\31\3\31\3\31\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\34")
        buf.write("\3\34\3\34\3\34\3\34\3\34\3\34\3\35\3\35\3\35\3\35\3\36")
        buf.write("\3\36\3\36\3\36\3\37\3\37\3\37\3 \3 \3 \3 \3!\3!\3!\3")
        buf.write("!\3\"\3\"\3#\3#\3$\3$\3%\3%\3&\3&\3\'\3\'\3(\3(\3)\3)")
        buf.write("\3*\3*\3+\3+\3,\3,\3-\3-\3.\3.\3/\3/\3\60\3\60\3\61\3")
        buf.write("\61\3\62\3\62\3\63\3\63\3\64\3\64\3\65\3\65\3\66\3\66")
        buf.write("\3\67\3\67\38\38\39\39\3:\3:\3;\3;\3<\3<\3=\3=\3>\3>\3")
        buf.write(">\3?\3?\3@\3@\3@\3A\3A\3B\3B\3C\3C\3D\3D\3E\3E\3E\3F\3")
        buf.write("F\7F\u01bf\nF\fF\16F\u01c2\13F\3G\6G\u01c5\nG\rG\16G\u01c6")
        buf.write("\3G\3G\3H\3H\3I\3I\3J\3J\3K\3K\3L\3L\3M\3M\3N\3N\3N\3")
        buf.write("O\3O\3P\6P\u01dd\nP\rP\16P\u01de\3Q\6Q\u01e2\nQ\rQ\16")
        buf.write("Q\u01e3\3Q\3Q\7Q\u01e8\nQ\fQ\16Q\u01eb\13Q\3R\7R\u01ee")
        buf.write("\nR\fR\16R\u01f1\13R\3R\3R\6R\u01f5\nR\rR\16R\u01f6\3")
        buf.write("S\6S\u01fa\nS\rS\16S\u01fb\3S\3S\5S\u0200\nS\3S\6S\u0203")
        buf.write("\nS\rS\16S\u0204\3T\6T\u0208\nT\rT\16T\u0209\3T\3T\6T")
        buf.write("\u020e\nT\rT\16T\u020f\3T\3T\5T\u0214\nT\3T\6T\u0217\n")
        buf.write("T\rT\16T\u0218\3U\3U\3U\3U\5U\u021f\nU\3V\3V\5V\u0223")
        buf.write("\nV\3W\3W\7W\u0227\nW\fW\16W\u022a\13W\3W\3W\4\u00b5\u00c1")
        buf.write("\2X\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r")
        buf.write("\31\16\33\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30")
        buf.write("/\31\61\32\63\33\65\34\67\359\36;\37= ?!A\"C\2E\2G\2I")
        buf.write("\2K\2M\2O\2Q\2S\2U\2W\2Y\2[\2]\2_\2a\2c\2e\2g\2i\2k\2")
        buf.write("m\2o\2q\2s\2u\2w#y${%}&\177\'\u0081(\u0083)\u0085*\u0087")
        buf.write("+\u0089,\u008b-\u008d.\u008f/\u0091\60\u0093\61\u0095")
        buf.write("\62\u0097\63\u0099\64\u009b\65\u009d\66\u009f\67\u00a1")
        buf.write("\2\u00a3\2\u00a5\2\u00a7\2\u00a98\u00ab9\u00ad:\3\2\"")
        buf.write("\5\2\f\f\17\17\"\"\4\2CCcc\4\2DDdd\4\2EEee\4\2FFff\4\2")
        buf.write("GGgg\4\2HHhh\4\2IIii\4\2JJjj\4\2KKkk\4\2LLll\4\2MMmm\4")
        buf.write("\2NNnn\4\2OOoo\4\2PPpp\4\2QQqq\4\2RRrr\4\2SSss\4\2TTt")
        buf.write("t\4\2UUuu\4\2VVvv\4\2WWww\4\2XXxx\4\2YYyy\4\2ZZzz\4\2")
        buf.write("[[{{\4\2\\\\||\5\2C\\aac|\6\2\62;C\\aac|\5\2\13\f\16\17")
        buf.write("\"\"\3\2\62;\6\2$$\60\60^^``\2\u0224\2\3\3\2\2\2\2\5\3")
        buf.write("\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2")
        buf.write("\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2")
        buf.write("\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2")
        buf.write("\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2")
        buf.write("\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3")
        buf.write("\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2")
        buf.write("\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2w\3\2")
        buf.write("\2\2\2y\3\2\2\2\2{\3\2\2\2\2}\3\2\2\2\2\177\3\2\2\2\2")
        buf.write("\u0081\3\2\2\2\2\u0083\3\2\2\2\2\u0085\3\2\2\2\2\u0087")
        buf.write("\3\2\2\2\2\u0089\3\2\2\2\2\u008b\3\2\2\2\2\u008d\3\2\2")
        buf.write("\2\2\u008f\3\2\2\2\2\u0091\3\2\2\2\2\u0093\3\2\2\2\2\u0095")
        buf.write("\3\2\2\2\2\u0097\3\2\2\2\2\u0099\3\2\2\2\2\u009b\3\2\2")
        buf.write("\2\2\u009d\3\2\2\2\2\u009f\3\2\2\2\2\u00a9\3\2\2\2\2\u00ab")
        buf.write("\3\2\2\2\2\u00ad\3\2\2\2\3\u00af\3\2\2\2\5\u00bd\3\2\2")
        buf.write("\2\7\u00c8\3\2\2\2\t\u00d3\3\2\2\2\13\u00d9\3\2\2\2\r")
        buf.write("\u00e2\3\2\2\2\17\u00e6\3\2\2\2\21\u00e9\3\2\2\2\23\u00f0")
        buf.write("\3\2\2\2\25\u00f3\3\2\2\2\27\u00f6\3\2\2\2\31\u00fb\3")
        buf.write("\2\2\2\33\u0100\3\2\2\2\35\u0107\3\2\2\2\37\u010d\3\2")
        buf.write("\2\2!\u0113\3\2\2\2#\u0117\3\2\2\2%\u0120\3\2\2\2\'\u012a")
        buf.write("\3\2\2\2)\u012e\3\2\2\2+\u0133\3\2\2\2-\u0139\3\2\2\2")
        buf.write("/\u013f\3\2\2\2\61\u0142\3\2\2\2\63\u0147\3\2\2\2\65\u014f")
        buf.write("\3\2\2\2\67\u0157\3\2\2\29\u015e\3\2\2\2;\u0162\3\2\2")
        buf.write("\2=\u0166\3\2\2\2?\u0169\3\2\2\2A\u016d\3\2\2\2C\u0171")
        buf.write("\3\2\2\2E\u0173\3\2\2\2G\u0175\3\2\2\2I\u0177\3\2\2\2")
        buf.write("K\u0179\3\2\2\2M\u017b\3\2\2\2O\u017d\3\2\2\2Q\u017f\3")
        buf.write("\2\2\2S\u0181\3\2\2\2U\u0183\3\2\2\2W\u0185\3\2\2\2Y\u0187")
        buf.write("\3\2\2\2[\u0189\3\2\2\2]\u018b\3\2\2\2_\u018d\3\2\2\2")
        buf.write("a\u018f\3\2\2\2c\u0191\3\2\2\2e\u0193\3\2\2\2g\u0195\3")
        buf.write("\2\2\2i\u0197\3\2\2\2k\u0199\3\2\2\2m\u019b\3\2\2\2o\u019d")
        buf.write("\3\2\2\2q\u019f\3\2\2\2s\u01a1\3\2\2\2u\u01a3\3\2\2\2")
        buf.write("w\u01a5\3\2\2\2y\u01a7\3\2\2\2{\u01a9\3\2\2\2}\u01ac\3")
        buf.write("\2\2\2\177\u01ae\3\2\2\2\u0081\u01b1\3\2\2\2\u0083\u01b3")
        buf.write("\3\2\2\2\u0085\u01b5\3\2\2\2\u0087\u01b7\3\2\2\2\u0089")
        buf.write("\u01b9\3\2\2\2\u008b\u01bc\3\2\2\2\u008d\u01c4\3\2\2\2")
        buf.write("\u008f\u01ca\3\2\2\2\u0091\u01cc\3\2\2\2\u0093\u01ce\3")
        buf.write("\2\2\2\u0095\u01d0\3\2\2\2\u0097\u01d2\3\2\2\2\u0099\u01d4")
        buf.write("\3\2\2\2\u009b\u01d6\3\2\2\2\u009d\u01d9\3\2\2\2\u009f")
        buf.write("\u01dc\3\2\2\2\u00a1\u01e1\3\2\2\2\u00a3\u01ef\3\2\2\2")
        buf.write("\u00a5\u01f9\3\2\2\2\u00a7\u0207\3\2\2\2\u00a9\u021e\3")
        buf.write("\2\2\2\u00ab\u0222\3\2\2\2\u00ad\u0224\3\2\2\2\u00af\u00b0")
        buf.write("\7*\2\2\u00b0\u00b1\7,\2\2\u00b1\u00b5\3\2\2\2\u00b2\u00b4")
        buf.write("\13\2\2\2\u00b3\u00b2\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5")
        buf.write("\u00b6\3\2\2\2\u00b5\u00b3\3\2\2\2\u00b6\u00b8\3\2\2\2")
        buf.write("\u00b7\u00b5\3\2\2\2\u00b8\u00b9\7,\2\2\u00b9\u00ba\7")
        buf.write("+\2\2\u00ba\u00bb\3\2\2\2\u00bb\u00bc\b\2\2\2\u00bc\4")
        buf.write("\3\2\2\2\u00bd\u00c1\7}\2\2\u00be\u00c0\13\2\2\2\u00bf")
        buf.write("\u00be\3\2\2\2\u00c0\u00c3\3\2\2\2\u00c1\u00c2\3\2\2\2")
        buf.write("\u00c1\u00bf\3\2\2\2\u00c2\u00c4\3\2\2\2\u00c3\u00c1\3")
        buf.write("\2\2\2\u00c4\u00c5\7\177\2\2\u00c5\u00c6\3\2\2\2\u00c6")
        buf.write("\u00c7\b\3\2\2\u00c7\6\3\2\2\2\u00c8\u00c9\7\61\2\2\u00c9")
        buf.write("\u00ca\7\61\2\2\u00ca\u00ce\3\2\2\2\u00cb\u00cd\n\2\2")
        buf.write("\2\u00cc\u00cb\3\2\2\2\u00cd\u00d0\3\2\2\2\u00ce\u00cc")
        buf.write("\3\2\2\2\u00ce\u00cf\3\2\2\2\u00cf\u00d1\3\2\2\2\u00d0")
        buf.write("\u00ce\3\2\2\2\u00d1\u00d2\b\4\2\2\u00d2\b\3\2\2\2\u00d3")
        buf.write("\u00d4\5E#\2\u00d4\u00d5\5e\63\2\u00d5\u00d6\5K&\2\u00d6")
        buf.write("\u00d7\5C\"\2\u00d7\u00d8\5W,\2\u00d8\n\3\2\2\2\u00d9")
        buf.write("\u00da\5G$\2\u00da\u00db\5_\60\2\u00db\u00dc\5]/\2\u00dc")
        buf.write("\u00dd\5i\65\2\u00dd\u00de\5S*\2\u00de\u00df\5]/\2\u00df")
        buf.write("\u00e0\5k\66\2\u00e0\u00e1\5K&\2\u00e1\f\3\2\2\2\u00e2")
        buf.write("\u00e3\5M\'\2\u00e3\u00e4\5_\60\2\u00e4\u00e5\5e\63\2")
        buf.write("\u00e5\16\3\2\2\2\u00e6\u00e7\5i\65\2\u00e7\u00e8\5_\60")
        buf.write("\2\u00e8\20\3\2\2\2\u00e9\u00ea\5I%\2\u00ea\u00eb\5_\60")
        buf.write("\2\u00eb\u00ec\5o8\2\u00ec\u00ed\5]/\2\u00ed\u00ee\5i")
        buf.write("\65\2\u00ee\u00ef\5_\60\2\u00ef\22\3\2\2\2\u00f0\u00f1")
        buf.write("\5I%\2\u00f1\u00f2\5_\60\2\u00f2\24\3\2\2\2\u00f3\u00f4")
        buf.write("\5S*\2\u00f4\u00f5\5M\'\2\u00f5\26\3\2\2\2\u00f6\u00f7")
        buf.write("\5i\65\2\u00f7\u00f8\5Q)\2\u00f8\u00f9\5K&\2\u00f9\u00fa")
        buf.write("\5]/\2\u00fa\30\3\2\2\2\u00fb\u00fc\5K&\2\u00fc\u00fd")
        buf.write("\5Y-\2\u00fd\u00fe\5g\64\2\u00fe\u00ff\5K&\2\u00ff\32")
        buf.write("\3\2\2\2\u0100\u0101\5e\63\2\u0101\u0102\5K&\2\u0102\u0103")
        buf.write("\5i\65\2\u0103\u0104\5k\66\2\u0104\u0105\5e\63\2\u0105")
        buf.write("\u0106\5]/\2\u0106\34\3\2\2\2\u0107\u0108\5o8\2\u0108")
        buf.write("\u0109\5Q)\2\u0109\u010a\5S*\2\u010a\u010b\5Y-\2\u010b")
        buf.write("\u010c\5K&\2\u010c\36\3\2\2\2\u010d\u010e\5E#\2\u010e")
        buf.write("\u010f\5K&\2\u010f\u0110\5O(\2\u0110\u0111\5S*\2\u0111")
        buf.write("\u0112\5]/\2\u0112 \3\2\2\2\u0113\u0114\5K&\2\u0114\u0115")
        buf.write("\5]/\2\u0115\u0116\5I%\2\u0116\"\3\2\2\2\u0117\u0118\5")
        buf.write("M\'\2\u0118\u0119\5k\66\2\u0119\u011a\5]/\2\u011a\u011b")
        buf.write("\5G$\2\u011b\u011c\5i\65\2\u011c\u011d\5S*\2\u011d\u011e")
        buf.write("\5_\60\2\u011e\u011f\5]/\2\u011f$\3\2\2\2\u0120\u0121")
        buf.write("\5a\61\2\u0121\u0122\5e\63\2\u0122\u0123\5_\60\2\u0123")
        buf.write("\u0124\5G$\2\u0124\u0125\5K&\2\u0125\u0126\5I%\2\u0126")
        buf.write("\u0127\5k\66\2\u0127\u0128\5e\63\2\u0128\u0129\5K&\2\u0129")
        buf.write("&\3\2\2\2\u012a\u012b\5m\67\2\u012b\u012c\5C\"\2\u012c")
        buf.write("\u012d\5e\63\2\u012d(\3\2\2\2\u012e\u012f\5i\65\2\u012f")
        buf.write("\u0130\5e\63\2\u0130\u0131\5k\66\2\u0131\u0132\5K&\2\u0132")
        buf.write("*\3\2\2\2\u0133\u0134\5M\'\2\u0134\u0135\5C\"\2\u0135")
        buf.write("\u0136\5Y-\2\u0136\u0137\5g\64\2\u0137\u0138\5K&\2\u0138")
        buf.write(",\3\2\2\2\u0139\u013a\5C\"\2\u013a\u013b\5e\63\2\u013b")
        buf.write("\u013c\5e\63\2\u013c\u013d\5C\"\2\u013d\u013e\5s:\2\u013e")
        buf.write(".\3\2\2\2\u013f\u0140\5_\60\2\u0140\u0141\5M\'\2\u0141")
        buf.write("\60\3\2\2\2\u0142\u0143\5e\63\2\u0143\u0144\5K&\2\u0144")
        buf.write("\u0145\5C\"\2\u0145\u0146\5Y-\2\u0146\62\3\2\2\2\u0147")
        buf.write("\u0148\5E#\2\u0148\u0149\5_\60\2\u0149\u014a\5_\60\2\u014a")
        buf.write("\u014b\5Y-\2\u014b\u014c\5K&\2\u014c\u014d\5C\"\2\u014d")
        buf.write("\u014e\5]/\2\u014e\64\3\2\2\2\u014f\u0150\5S*\2\u0150")
        buf.write("\u0151\5]/\2\u0151\u0152\5i\65\2\u0152\u0153\5K&\2\u0153")
        buf.write("\u0154\5O(\2\u0154\u0155\5K&\2\u0155\u0156\5e\63\2\u0156")
        buf.write("\66\3\2\2\2\u0157\u0158\5g\64\2\u0158\u0159\5i\65\2\u0159")
        buf.write("\u015a\5e\63\2\u015a\u015b\5S*\2\u015b\u015c\5]/\2\u015c")
        buf.write("\u015d\5O(\2\u015d8\3\2\2\2\u015e\u015f\5]/\2\u015f\u0160")
        buf.write("\5_\60\2\u0160\u0161\5i\65\2\u0161:\3\2\2\2\u0162\u0163")
        buf.write("\5C\"\2\u0163\u0164\5]/\2\u0164\u0165\5I%\2\u0165<\3\2")
        buf.write("\2\2\u0166\u0167\5_\60\2\u0167\u0168\5e\63\2\u0168>\3")
        buf.write("\2\2\2\u0169\u016a\5I%\2\u016a\u016b\5S*\2\u016b\u016c")
        buf.write("\5m\67\2\u016c@\3\2\2\2\u016d\u016e\5[.\2\u016e\u016f")
        buf.write("\5_\60\2\u016f\u0170\5I%\2\u0170B\3\2\2\2\u0171\u0172")
        buf.write("\t\3\2\2\u0172D\3\2\2\2\u0173\u0174\t\4\2\2\u0174F\3\2")
        buf.write("\2\2\u0175\u0176\t\5\2\2\u0176H\3\2\2\2\u0177\u0178\t")
        buf.write("\6\2\2\u0178J\3\2\2\2\u0179\u017a\t\7\2\2\u017aL\3\2\2")
        buf.write("\2\u017b\u017c\t\b\2\2\u017cN\3\2\2\2\u017d\u017e\t\t")
        buf.write("\2\2\u017eP\3\2\2\2\u017f\u0180\t\n\2\2\u0180R\3\2\2\2")
        buf.write("\u0181\u0182\t\13\2\2\u0182T\3\2\2\2\u0183\u0184\t\f\2")
        buf.write("\2\u0184V\3\2\2\2\u0185\u0186\t\r\2\2\u0186X\3\2\2\2\u0187")
        buf.write("\u0188\t\16\2\2\u0188Z\3\2\2\2\u0189\u018a\t\17\2\2\u018a")
        buf.write("\\\3\2\2\2\u018b\u018c\t\20\2\2\u018c^\3\2\2\2\u018d\u018e")
        buf.write("\t\21\2\2\u018e`\3\2\2\2\u018f\u0190\t\22\2\2\u0190b\3")
        buf.write("\2\2\2\u0191\u0192\t\23\2\2\u0192d\3\2\2\2\u0193\u0194")
        buf.write("\t\24\2\2\u0194f\3\2\2\2\u0195\u0196\t\25\2\2\u0196h\3")
        buf.write("\2\2\2\u0197\u0198\t\26\2\2\u0198j\3\2\2\2\u0199\u019a")
        buf.write("\t\27\2\2\u019al\3\2\2\2\u019b\u019c\t\30\2\2\u019cn\3")
        buf.write("\2\2\2\u019d\u019e\t\31\2\2\u019ep\3\2\2\2\u019f\u01a0")
        buf.write("\t\32\2\2\u01a0r\3\2\2\2\u01a1\u01a2\t\33\2\2\u01a2t\3")
        buf.write("\2\2\2\u01a3\u01a4\t\34\2\2\u01a4v\3\2\2\2\u01a5\u01a6")
        buf.write("\7-\2\2\u01a6x\3\2\2\2\u01a7\u01a8\7,\2\2\u01a8z\3\2\2")
        buf.write("\2\u01a9\u01aa\7>\2\2\u01aa\u01ab\7@\2\2\u01ab|\3\2\2")
        buf.write("\2\u01ac\u01ad\7>\2\2\u01ad~\3\2\2\2\u01ae\u01af\7>\2")
        buf.write("\2\u01af\u01b0\7?\2\2\u01b0\u0080\3\2\2\2\u01b1\u01b2")
        buf.write("\7/\2\2\u01b2\u0082\3\2\2\2\u01b3\u01b4\7\61\2\2\u01b4")
        buf.write("\u0084\3\2\2\2\u01b5\u01b6\7?\2\2\u01b6\u0086\3\2\2\2")
        buf.write("\u01b7\u01b8\7@\2\2\u01b8\u0088\3\2\2\2\u01b9\u01ba\7")
        buf.write("@\2\2\u01ba\u01bb\7?\2\2\u01bb\u008a\3\2\2\2\u01bc\u01c0")
        buf.write("\t\35\2\2\u01bd\u01bf\t\36\2\2\u01be\u01bd\3\2\2\2\u01bf")
        buf.write("\u01c2\3\2\2\2\u01c0\u01be\3\2\2\2\u01c0\u01c1\3\2\2\2")
        buf.write("\u01c1\u008c\3\2\2\2\u01c2\u01c0\3\2\2\2\u01c3\u01c5\t")
        buf.write("\37\2\2\u01c4\u01c3\3\2\2\2\u01c5\u01c6\3\2\2\2\u01c6")
        buf.write("\u01c4\3\2\2\2\u01c6\u01c7\3\2\2\2\u01c7\u01c8\3\2\2\2")
        buf.write("\u01c8\u01c9\bG\2\2\u01c9\u008e\3\2\2\2\u01ca\u01cb\7")
        buf.write("]\2\2\u01cb\u0090\3\2\2\2\u01cc\u01cd\7_\2\2\u01cd\u0092")
        buf.write("\3\2\2\2\u01ce\u01cf\7<\2\2\u01cf\u0094\3\2\2\2\u01d0")
        buf.write("\u01d1\7*\2\2\u01d1\u0096\3\2\2\2\u01d2\u01d3\7+\2\2\u01d3")
        buf.write("\u0098\3\2\2\2\u01d4\u01d5\7=\2\2\u01d5\u009a\3\2\2\2")
        buf.write("\u01d6\u01d7\7\60\2\2\u01d7\u01d8\7\60\2\2\u01d8\u009c")
        buf.write("\3\2\2\2\u01d9\u01da\7.\2\2\u01da\u009e\3\2\2\2\u01db")
        buf.write("\u01dd\t \2\2\u01dc\u01db\3\2\2\2\u01dd\u01de\3\2\2\2")
        buf.write("\u01de\u01dc\3\2\2\2\u01de\u01df\3\2\2\2\u01df\u00a0\3")
        buf.write("\2\2\2\u01e0\u01e2\t \2\2\u01e1\u01e0\3\2\2\2\u01e2\u01e3")
        buf.write("\3\2\2\2\u01e3\u01e1\3\2\2\2\u01e3\u01e4\3\2\2\2\u01e4")
        buf.write("\u01e5\3\2\2\2\u01e5\u01e9\7\60\2\2\u01e6\u01e8\t \2\2")
        buf.write("\u01e7\u01e6\3\2\2\2\u01e8\u01eb\3\2\2\2\u01e9\u01e7\3")
        buf.write("\2\2\2\u01e9\u01ea\3\2\2\2\u01ea\u00a2\3\2\2\2\u01eb\u01e9")
        buf.write("\3\2\2\2\u01ec\u01ee\t \2\2\u01ed\u01ec\3\2\2\2\u01ee")
        buf.write("\u01f1\3\2\2\2\u01ef\u01ed\3\2\2\2\u01ef\u01f0\3\2\2\2")
        buf.write("\u01f0\u01f2\3\2\2\2\u01f1\u01ef\3\2\2\2\u01f2\u01f4\7")
        buf.write("\60\2\2\u01f3\u01f5\t \2\2\u01f4\u01f3\3\2\2\2\u01f5\u01f6")
        buf.write("\3\2\2\2\u01f6\u01f4\3\2\2\2\u01f6\u01f7\3\2\2\2\u01f7")
        buf.write("\u00a4\3\2\2\2\u01f8\u01fa\t \2\2\u01f9\u01f8\3\2\2\2")
        buf.write("\u01fa\u01fb\3\2\2\2\u01fb\u01f9\3\2\2\2\u01fb\u01fc\3")
        buf.write("\2\2\2\u01fc\u01fd\3\2\2\2\u01fd\u01ff\t\7\2\2\u01fe\u0200")
        buf.write("\7/\2\2\u01ff\u01fe\3\2\2\2\u01ff\u0200\3\2\2\2\u0200")
        buf.write("\u0202\3\2\2\2\u0201\u0203\t \2\2\u0202\u0201\3\2\2\2")
        buf.write("\u0203\u0204\3\2\2\2\u0204\u0202\3\2\2\2\u0204\u0205\3")
        buf.write("\2\2\2\u0205\u00a6\3\2\2\2\u0206\u0208\t \2\2\u0207\u0206")
        buf.write("\3\2\2\2\u0208\u0209\3\2\2\2\u0209\u0207\3\2\2\2\u0209")
        buf.write("\u020a\3\2\2\2\u020a\u020b\3\2\2\2\u020b\u020d\7\60\2")
        buf.write("\2\u020c\u020e\t \2\2\u020d\u020c\3\2\2\2\u020e\u020f")
        buf.write("\3\2\2\2\u020f\u020d\3\2\2\2\u020f\u0210\3\2\2\2\u0210")
        buf.write("\u0211\3\2\2\2\u0211\u0213\t\7\2\2\u0212\u0214\7/\2\2")
        buf.write("\u0213\u0212\3\2\2\2\u0213\u0214\3\2\2\2\u0214\u0216\3")
        buf.write("\2\2\2\u0215\u0217\t \2\2\u0216\u0215\3\2\2\2\u0217\u0218")
        buf.write("\3\2\2\2\u0218\u0216\3\2\2\2\u0218\u0219\3\2\2\2\u0219")
        buf.write("\u00a8\3\2\2\2\u021a\u021f\5\u00a1Q\2\u021b\u021f\5\u00a3")
        buf.write("R\2\u021c\u021f\5\u00a5S\2\u021d\u021f\5\u00a7T\2\u021e")
        buf.write("\u021a\3\2\2\2\u021e\u021b\3\2\2\2\u021e\u021c\3\2\2\2")
        buf.write("\u021e\u021d\3\2\2\2\u021f\u00aa\3\2\2\2\u0220\u0223\5")
        buf.write(")\25\2\u0221\u0223\5+\26\2\u0222\u0220\3\2\2\2\u0222\u0221")
        buf.write("\3\2\2\2\u0223\u00ac\3\2\2\2\u0224\u0228\7$\2\2\u0225")
        buf.write("\u0227\t!\2\2\u0226\u0225\3\2\2\2\u0227\u022a\3\2\2\2")
        buf.write("\u0228\u0226\3\2\2\2\u0228\u0229\3\2\2\2\u0229\u022b\3")
        buf.write("\2\2\2\u022a\u0228\3\2\2\2\u022b\u022c\7$\2\2\u022c\u00ae")
        buf.write("\3\2\2\2\30\2\u00b5\u00c1\u00ce\u01c0\u01c6\u01de\u01e3")
        buf.write("\u01e9\u01ef\u01f6\u01fb\u01ff\u0204\u0209\u020f\u0213")
        buf.write("\u0218\u021e\u0222\u0226\u0228\3\b\2\2")
        return buf.getvalue()


class MPLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    TRADI_CMT = 1
    BLOCK_CMT = 2
    LINE_CMT = 3
    BREAK = 4
    CONTINUE = 5
    FOR = 6
    TO = 7
    DOWNTO = 8
    DO = 9
    IF = 10
    THEN = 11
    ELSE = 12
    RETURN = 13
    WHILE = 14
    BEGIN = 15
    END = 16
    FUNCTION = 17
    PROCEDURE = 18
    VAR = 19
    TRUE = 20
    FALSE = 21
    ARRAY = 22
    OF = 23
    REAL = 24
    BOOLEAN = 25
    INTEGER = 26
    STRING = 27
    NOT = 28
    AND = 29
    OR = 30
    DIV = 31
    MOD = 32
    ADD = 33
    MUL = 34
    NOTEQUAL = 35
    LESSTHAN = 36
    LESSEQUAL = 37
    SUB = 38
    DIVISION = 39
    EQUA = 40
    GREATERTHAN = 41
    GREATEREQUAL = 42
    ID = 43
    WS = 44
    LSB = 45
    RSB = 46
    COLON = 47
    LB = 48
    RB = 49
    SEMI = 50
    DD = 51
    COMMA = 52
    INTLIT = 53
    FLOATLIT = 54
    BOOLEANLIT = 55
    STRLIT = 56

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'*'", "'<>'", "'<'", "'<='", "'-'", "'/'", "'='", "'>'", 
            "'>='", "'['", "']'", "':'", "'('", "')'", "';'", "'..'", "','" ]

    symbolicNames = [ "<INVALID>",
            "TRADI_CMT", "BLOCK_CMT", "LINE_CMT", "BREAK", "CONTINUE", "FOR", 
            "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", "WHILE", 
            "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", "TRUE", "FALSE", 
            "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", "STRING", "NOT", 
            "AND", "OR", "DIV", "MOD", "ADD", "MUL", "NOTEQUAL", "LESSTHAN", 
            "LESSEQUAL", "SUB", "DIVISION", "EQUA", "GREATERTHAN", "GREATEREQUAL", 
            "ID", "WS", "LSB", "RSB", "COLON", "LB", "RB", "SEMI", "DD", 
            "COMMA", "INTLIT", "FLOATLIT", "BOOLEANLIT", "STRLIT" ]

    ruleNames = [ "TRADI_CMT", "BLOCK_CMT", "LINE_CMT", "BREAK", "CONTINUE", 
                  "FOR", "TO", "DOWNTO", "DO", "IF", "THEN", "ELSE", "RETURN", 
                  "WHILE", "BEGIN", "END", "FUNCTION", "PROCEDURE", "VAR", 
                  "TRUE", "FALSE", "ARRAY", "OF", "REAL", "BOOLEAN", "INTEGER", 
                  "STRING", "NOT", "AND", "OR", "DIV", "MOD", "A", "B", 
                  "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", 
                  "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", 
                  "Y", "Z", "ADD", "MUL", "NOTEQUAL", "LESSTHAN", "LESSEQUAL", 
                  "SUB", "DIVISION", "EQUA", "GREATERTHAN", "GREATEREQUAL", 
                  "ID", "WS", "LSB", "RSB", "COLON", "LB", "RB", "SEMI", 
                  "DD", "COMMA", "INTLIT", "CASE1", "CASE2", "CASE3", "CASE4", 
                  "FLOATLIT", "BOOLEANLIT", "STRLIT" ]

    grammarFileName = "MP.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.7.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


