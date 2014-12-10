import codecs


def copy_file(filename, source_directory, destination_directory):
    u"""Copy file from source to destination"""
    original = codecs.open(u"%s/%s" % (source_directory, filename))
    lines = original.readlines()
    copy = codecs.open(u"%s/%s" % (destination_directory, filename), "w")
    copy.writelines(lines)
    original.close()
    copy.close()
