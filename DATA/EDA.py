import pandas as pd
from ydata_profiling import ProfileReport
import os

# 1. تحميل البيانات
file_path = "D:\DATA ANALYST\HR TABLEAU\projects\projects\hr-dashboard-project\Cleaned.csv"  # غير اسم الملف حسب بياناتك
df = pd.read_csv(file_path)

# 2. معاينة أول 5 صفوف للتأكد من التحميل
print("✅ Preview of the dataset:")
print(df.head())

# 3. توليد تقرير الـ Profiling
profile = ProfileReport(df, title="🔍 Data Profiling Report", explorative=True)

# 4. حفظ التقرير كـ HTML
output_file = "data_profiling_report.html"
profile.to_file(output_file=output_file)

print(f"📊 Profiling report generated successfully: {os.path.abspath(output_file)}")