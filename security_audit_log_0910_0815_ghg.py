# 代码生成时间: 2025-09-10 08:15:39
import pandas as pd
import logging
from datetime import datetime

# 配置日志
logging.basicConfig(filename='security_audit.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class SecurityAuditLogger:
    """安全审计日志类"""
    def __init__(self, log_file):
        """初始化审计日志文件"""
        self.log_file = log_file
        self.logger = logging.getLogger('SecurityAudit')

    def log_event(self, event_type, user, action, details):
        """记录安全事件到日志文件"""
        try:
            event = {
                'Event Type': event_type,
                'User': user,
                'Action': action,
                'Details': details,
                'Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            # 将事件记录到日志文件
            self.logger.info(f"{{'Event Type': '{event['Event Type']}', 'User': '{event['User']}', 'Action': '{event['Action']}', 'Details': '{event['Details']}', 'Timestamp': '{event['Timestamp']}'}")
        except Exception as e:
            self.logger.error(f"Error logging event: {str(e)}")

    def export_to_csv(self):
        """导出日志到CSV文件"""
        try:
            # 读取日志文件并转换为DataFrame
            with open(self.log_file, 'r') as file:
                lines = file.readlines()
            data = [line.strip() for line in lines]
            df = pd.DataFrame(data, columns=['Log Entry'])
            # 将DataFrame转换为CSV文件
            df.to_csv('security_audit.csv', index=False)
        except Exception as e:
            self.logger.error(f"Error exporting to CSV: {str(e)}")

# 示例用法
if __name__ == '__main__':
    audit_logger = SecurityAuditLogger('security_audit.log')
    audit_logger.log_event('Access', 'John Doe', 'Login', 'User logged in from IP 192.168.1.1')
    audit_logger.export_to_csv()