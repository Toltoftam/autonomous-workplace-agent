from datetime import datetime


class AuditLogger:

    def log(self, action, result):

        log_entry = {
            "timestamp":
                datetime.utcnow().isoformat(),
            "action": action,
            "result": result
        }

        print(log_entry)
