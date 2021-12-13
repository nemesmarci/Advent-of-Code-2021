from common import get_data, do_folds

print(len(do_folds(*get_data(), stop_at_first=True)))
