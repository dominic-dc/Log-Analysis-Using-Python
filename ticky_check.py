import re
import csv
import operator

def get_count():
    errors = {}
    per_user = {}
    fh = open("syslog.log")
    pattern = r": ([A-Z]+) ([\w ']+) [#\d\[\] ]*\(([\w\.]+)\)"
    for line in fh:
        match = re.search(pattern, line)
        message_type = match[1]
        message = match[2]
        username = match[3]
        # For errors checking and user count of errors
        if message_type == "ERROR":
            errors[message] = errors.get(message, 0) + 1
            if username in per_user:
                per_user[username][message_type] += 1
            else:
                per_user[username] = {"ERROR":1, "INFO":0}
        # User count of info
        else:
            if username in per_user:
                per_user[username][message_type] += 1
            else:
                per_user[username] = {"ERROR":0, "INFO":1}
    
    return errors, per_user

def sort_dict(errors, per_user):
    errors = sorted(errors.items(), key=operator.itemgetter(1), reverse=True)
    per_user = sorted(per_user.items())
    return errors, per_user

def export_to_csv(errors, per_user):
    with open("error_message.csv", "w") as csv_f:
        writer = csv.writer(csv_f)
        writer.writerow(["Error", "Count"])
        writer.writerows(errors)
    with open("user_statistics.csv", "w") as csv_f:
        writer = csv.writer(csv_f)
        writer.writerow(["Username", "INFO", "ERROR"])
        for item in per_user:
            writer.writerow([item[0], item[1]["INFO"], item[1]["ERROR"]])
    

errors, per_user = get_count()
errors, per_user = sort_dict(errors, per_user)
export_to_csv(errors, per_user)


print(per_user)
print("---------------------------------------------------------")
print(errors)
