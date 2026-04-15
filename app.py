import streamlit as st
import pandas as pd
from datetime import datetime

# 错误处理
try:
    import pandas as pd
except ImportError:
    import sys
    sys.path.append('/home/appuser')
    import pandas as pd


# 设置页面配置
st.set_page_config(
    page_title="数字游民签证助手",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 国家数据库（包含付费内容）
countries_db = {
    "葡萄牙": {
        # 免费内容
        "优势": ["欧盟身份", "税务优惠", "安全", "英语普及"],
        "劣势": ["生活成本较高", "语言障碍", "审批慢"],
        "收入要求": "每月€3040",
        "存款要求": "€9120",
        "每月生活费": "€800-1200",
        "税率": "10% (NHR计划)",
        "适合人群": ["高收入人群", "想拿欧盟身份", "重视安全"],
        "签证类型": "D7签证",
        "处理时间": "3-4个月",
        "匹配度": 0,
        
        # 付费内容
        "付费解读": {
            "资格与材料": {
                "职业要求": "葡萄牙D7签证对职业无严格限制，重点看被动收入或远程工作收入。程序员、设计师、自媒体、咨询顾问等远程工作完全符合条件。",
                "收入形式": "支持多种收入形式：工资、自由职业、股息、租金、退休金等。需提供6个月银行流水和收入证明，建议收入稳定。",
                "核心材料": [
                    "有效护照（有效期6个月以上）",
                    "无犯罪记录证明（双认证）",
                    "收入证明（6个月银行流水）",
                    "葡萄牙住址证明（租房合同）",
                    "健康保险（保额≥3万欧元）",
                    "动机信（说明移居目的）"
                ],
                "材料时效": "无犯罪记录证明需3个月内开具，银行流水需最近6个月，所有非英文文件需翻译认证。"
            },
            "生活与保障": {
                "医疗保障": "获得居留许可后可加入葡萄牙公共医疗系统(SNS)，年费约300-400欧元。私立保险约50-100欧元/月，看病报销80-90%。",
                "住房情况": "里斯本单间公寓€600-900/月，波尔图€400-700/月。建议先短租3个月适应，再决定长租。",
                "家庭随行": "配偶和18岁以下子女可一同申请，需提供结婚证明和子女出生证明，每增加一人需额外证明收入能力。",
                "教育资源": "公立学校免费（葡萄牙语教学），国际学校€6000-15000/年（英语教学），适合带娃家庭。"
            },
            "税务与身份": {
                "税务政策": "NHR计划（新居民税收优惠）前10年享受优惠：外国收入免税（部分国家），养老金按10%征税，高附加值职业收入按20%征税。",
                "居住要求": "第一年住满7天，之后每两年住满14天。5年后可申请永居或入籍，需通过基础葡萄牙语考试（A2水平）。",
                "入籍优势": "葡萄牙护照全球排名第4，免签186国，可在欧盟任意国家工作居住。"
            },
            "风险与注意事项": {
                "签证期限": "首次获批4个月有效期入境签证，入境后需4个月内申请居留许可，有效期2年，可续签3年。",
                "常见坑点": [
                    "收入证明不稳定容易被拒",
                    "租房合同需真实有效，假合同会被查",
                    "保险必须在葡萄牙有效",
                    "材料翻译需认证，自己翻译无效"
                ],
                "出入境注意": "持有D7签证可自由出入申根区，但需满足居住要求。建议保留出入境记录和居住证明。",
                "续签要点": "续签需证明仍有稳定收入、有住址、有保险，建议提前3个月准备材料。"
            }
        }
    },
    "西班牙": {
        # 免费内容
        "优势": ["欧盟身份", "生活成本低", "气候好", "文化丰富"],
        "劣势": ["失业率较高", "语言障碍", "官僚复杂"],
        "收入要求": "每月€2151",
        "存款要求": "€25812",
        "每月生活费": "€600-900",
        "税率": "24% (前6年)",
        "适合人群": ["预算有限", "喜欢文化", "追求性价比"],
        "签证类型": "非盈利签证",
        "处理时间": "2-3个月",
        "匹配度": 0,
        
        # 付费内容
        "付费解读": {
            "资格与材料": {
                "职业要求": "西班牙非盈利签证不限制职业，但要求证明有稳定被动收入或远程工作收入，不能占用本地就业机会。",
                "收入形式": "接受租金、股息、退休金、远程工作收入等。存款证明很重要，€25812是最低要求，建议更多。",
                "核心材料": [
                    "有效护照",
                    "无犯罪记录证明（双认证，3个月内）",
                    "健康证明（指定医院体检）",
                    "收入证明（6个月流水）",
                    "存款证明（€25812以上）",
                    "西班牙住址证明（租房合同）",
                    "私立健康保险（全额覆盖）"
                ],
                "材料时效": "体检证明需3个月内，无犯罪记录3个月内，银行流水最近6个月。"
            },
            "生活与保障": {
                "医疗保障": "私立保险约€50-150/月，保额需全额覆盖。获得居留后可申请公立医疗，但非盈利签证持有者有限制。",
                "住房情况": "马德里单间€500-800/月，巴塞罗那€600-900/月，瓦伦西亚€400-600/月。租房市场活跃，选择多。",
                "家庭随行": "配偶和子女可一同申请，需证明额外经济能力（每人约€6000/年）。子女可享受公立教育。",
                "教育资源": "公立学校免费（西班牙语），国际学校€5000-12000/年。大学学费低廉，欧盟学生约€1000-3000/年。"
            },
            "税务与身份": {
                "税务政策": "前6年按24%统一税率（境外收入），之后按累进税率19-45%。成为税务居民需住满183天/年。",
                "居住要求": "无严格居住要求，但续签需证明有实际居住。5年可申请永居，10年可申请入籍。",
                "入籍要求": "需通过西班牙语考试（DELE A2）和文化考试，放弃原国籍（部分国家例外）。"
            },
            "风险与注意事项": {
                "签证期限": "首次获批1年，续签2年+2年。每年需住满183天才能维持税务居民身份。",
                "常见坑点": [
                    "存款证明要求严格，需真实存款",
                    "不能工作，违规会被取消签证",
                    "保险必须全额覆盖，不能有病史除外",
                    "续签时收入证明要求更严格"
                ],
                "出入境注意": "无出入境限制，但需注意居住天数计算。建议保留机票、住宿证明。",
                "续签要点": "需证明持续收入、实际居住、有效保险。建议每年住满6个月以上。"
            }
        }
    },
    "泰国": {
        # 免费内容
        "优势": ["生活成本极低", "美食丰富", "网络好", "华人多"],
        "劣势": ["非永久身份", "语言障碍", "气候炎热"],
        "收入要求": "每月$2000",
        "存款要求": "$10000",
        "每月生活费": "$300-500",
        "税率": "0% (境外收入免税)",
        "适合人群": ["预算极低", "喜欢热带", "吃辣爱好者"],
        "签证类型": "LTR签证",
        "处理时间": "1个月",
        "匹配度": 0,
        
        # 付费内容
        "付费解读": {
            "资格与材料": {
                "职业要求": "泰国LTR签证针对高技能专业人士，包括数字游民、远程工作者。需提供专业技能证明或工作经验。",
                "收入形式": "接受工资、自由职业、投资收入等。需证明过去2年平均月收入$2000以上，或存款$10000+年收入$24000。",
                "核心材料": [
                    "有效护照（6个月以上）",
                    "无犯罪记录证明（双认证）",
                    "学历证明或工作经验证明",
                    "收入证明（2年税单或银行流水）",
                    "健康保险（保额$50000以上）",
                    "泰国住址证明（租房合同或酒店预订单）"
                ],
                "材料时效": "无犯罪记录6个月内，其他材料需最新版本。"
            },
            "生活与保障": {
                "医疗保障": "私立医院性价比高，门诊$20-50，住院$50-100/天。建议购买国际保险$500-1000/年。",
                "住房情况": "曼谷单间$200-400/月，清迈$150-300/月，普吉$250-450/月。短租灵活，长租更便宜。",
                "家庭随行": "配偶和20岁以下子女可随行，需额外证明经济能力。泰国国际学校质量高，$3000-8000/年。",
                "华人社区": "曼谷、清迈华人多，有唐人街、华人超市、中餐馆，生活便利。"
            },
            "税务与身份": {
                "税务政策": "境外收入免税，境内收入按累进税率5-35%。成为税务居民需住满180天/年。",
                "居住要求": "LTR签证有效期10年，可续签。每年需向移民局报到，无严格居住天数要求。",
                "身份优势": "LTR签证不是永居，但可长期居住。不能自动获得工作许可，需单独申请。"
            },
            "风险与注意事项": {
                "签证期限": "首次获批5年，可续签5年。需每年报到，地址变更需及时通知移民局。",
                "常见坑点": [
                    "收入证明要求严格，需持续稳定收入",
                    "保险必须覆盖泰国，且保额充足",
                    "不能从事本地工作，只能远程工作",
                    "地址变更需及时报告，否则罚款"
                ],
                "出入境注意": "可自由出入境，但建议保留居住证明。每次入境需携带签证相关文件。",
                "续签要点": "需证明持续收入、有效保险、住址。建议每年住满3个月以上。"
            }
        }
    },
    "墨西哥": {
        # 免费内容
        "优势": ["美国近", "生活成本低", "美食好", "文化丰富"],
        "劣势": ["安全问题", "语言障碍", "基础设施不稳定"],
        "收入要求": "每月$1500",
        "存款要求": "$2700",
        "每月生活费": "$400-600",
        "税率": "0% (境外收入免税)",
        "适合人群": ["想去美洲", "预算有限", "喜欢墨西哥菜"],
        "签证类型": "临时居民签证",
        "处理时间": "1-2个月",
        "匹配度": 0,
        
        # 付费内容
        "付费解读": {
            "资格与材料": {
                "职业要求": "墨西哥临时居民签证对职业无限制，接受远程工作、自由职业、投资收入等。重点证明经济能力。",
                "收入形式": "接受各种收入形式，要求较低。月收入$1500或存款$27000（过去12个月平均）。",
                "核心材料": [
                    "有效护照",
                    "无犯罪记录证明（海牙认证）",
                    "经济能力证明（银行流水或存款证明）",
                    "墨西哥住址证明（租房合同）",
                    "健康保险（覆盖墨西哥）",
                    "签证申请表和照片"
                ],
                "材料时效": "无犯罪记录3个月内，银行流水最近6个月。"
            },
            "生活与保障": {
                "医疗保障": "私立医院便宜，门诊$30-50，住院$100-200/天。建议购买国际保险$600-1200/年。",
                "住房情况": "墨西哥城单间$300-500/月，坎昆$400-600/月， Playa del Carmen $350-550/月。",
                "家庭随行": "配偶和子女可申请家属签证，需证明额外经济能力。子女可享受公立教育。",
                "安全注意": "选择安全区域居住，避免夜间单独外出，注意财产安全。建议住外国人聚集区。"
            },
            "税务与身份": {
                "税务政策": "境外收入免税，境内收入按累进税率0-35%。成为税务居民需住满183天/年。",
                "居住要求": "临时居民签证有效期1-4年，可续签。住满4年可申请永居，住满5年可申请入籍。",
                "入籍优势": "墨西哥护照免签150+国，包括申根区、英国、日本等。"
            },
            "风险与注意事项": {
                "签证期限": "首次获批1年，可续签1-3年。需证明持续经济能力，不能工作。",
                "常见坑点": [
                    "安全是最大问题，需选择安全区域",
                    "不能从事本地工作，只能远程",
                    "基础设施不稳定，网络可能中断",
                    "官僚效率低，办事需耐心"
                ],
                "出入境注意": "可自由出入境，但需注意签证有效期。建议提前2个月续签。",
                "续签要点": "需证明持续经济能力、住址、保险。建议保留所有账单和合同。"
            }
        }
    },
    "克罗地亚": {
        # 免费内容
        "优势": ["欧盟身份", "生活成本低", "海滩美", "英语普及"],
        "劣势": ["冬季寒冷", "经济不发达", "社交圈小"],
        "收入要求": "每月€2300",
        "存款要求": "€27600",
        "每月生活费": "€500-700",
        "税率": "12% (境外收入)",
        "适合人群": ["喜欢海滩", "预算有限", "想拿欧盟身份"],
        "签证类型": "数字游民签证",
        "处理时间": "1个月",
        "匹配度": 0,
        
        # 付费内容
        "付费解读": {
            "资格与材料": {
                "职业要求": "克罗地亚数字游民签证明确针对远程工作者，需提供雇佣合同或客户证明，证明工作可远程完成。",
                "收入形式": "接受远程工资、自由职业收入等。月收入€2300或存款€27600+年收入€27600。",
                "核心材料": [
                    "有效护照",
                    "无犯罪记录证明（海牙认证，3个月内）",
                    "远程工作证明（雇佣合同或客户证明）",
                    "收入证明（3个月银行流水）",
                    "克罗地亚住址证明",
                    "健康保险（保额€30000以上）",
                    "签证申请表"
                ],
                "材料时效": "无犯罪记录3个月内，银行流水最近3个月。"
            },
            "生活与保障": {
                "医疗保障": "公立医疗质量一般，建议购买私立保险€30-80/月。主要城市医疗设施较好。",
                "住房情况": "萨格勒布单间€300-500/月，沿海城市€400-600/月。夏季旅游旺季房租上涨。",
                "家庭随行": "配偶和子女可申请，需证明额外经济能力。子女可享受公立教育。",
                "季节影响": "冬季寒冷多雨，夏季炎热干燥。旅游旺季人多，淡季安静。"
            },
            "税务与身份": {
                "税务政策": "境外收入按12%统一税率，境内收入按累进税率。成为税务居民需住满183天/年。",
                "居住要求": "数字游民签证有效期1年，可续签1年。无永居路径，需转其他签证类型。",
                "签证限制": "不能工作于克罗地亚公司，只能为外国公司远程工作。"
            },
            "风险与注意事项": {
                "签证期限": "有效期1年，可续签1次。总共最多2年，之后需离开或转其他签证。",
                "常见坑点": [
                    "签证期限短，无永居路径",
                    "冬季寒冷，不适合怕冷的人",
                    "经济不发达，工作机会少",
                    "社交圈小，外国人少"
                ],
                "出入境注意": "可自由出入申根区，但需满足居住要求。建议保留居住证明。",
                "续签要点": "需证明持续远程工作、收入、住址。续签只能1次，需提前规划后续签证。"
            }
        }
    }
}

def calculate_match(user_profile):
    """计算匹配度"""
    matches = []
    
    for country, data in countries_db.items():
        score = 50  # 基础分
        
        # 收入匹配
        monthly_income = user_profile.get("monthly_income", 0)
        if monthly_income >= 30000:  # 高收入
            if country in ["葡萄牙", "西班牙", "克罗地亚"]:
                score += 15
        elif monthly_income >= 15000:  # 中等收入
            if country in ["西班牙", "克罗地亚", "墨西哥"]:
                score += 15
        else:  # 低收入
            if country in ["泰国", "墨西哥"]:
                score += 15
        
        # 偏好匹配 - 多偏好加权
        preference = user_profile.get("preference", "")
        custom_preference = user_profile.get("custom_preference", "")
        
        # 基础偏好匹配
        if "海滩" in preference and country in ["泰国", "克罗地亚"]:
            score += 8
        if "城市" in preference and country in ["葡萄牙", "西班牙"]:
            score += 8
        if "低成本" in preference and country in ["泰国", "墨西哥", "克罗地亚"]:
            score += 10
        if "安全" in preference and country in ["葡萄牙", "克罗地亚"]:
            score += 8
        if "网络好" in preference and country in ["泰国", "葡萄牙"]:
            score += 8
        if "气候温和" in preference and country in ["葡萄牙", "西班牙", "克罗地亚"]:
            score += 6
        if "华人社区" in preference and country in ["泰国"]:
            score += 8
        if "英语普及" in preference and country in ["葡萄牙", "克罗地亚"]:
            score += 6
        if "教育资源" in preference and country in ["葡萄牙", "西班牙"]:
            score += 6
        if "医疗水平" in preference and country in ["葡萄牙", "西班牙", "泰国"]:
            score += 6
        if "美食丰富" in preference and country in ["泰国", "墨西哥", "西班牙"]:
            score += 6
        if "文化丰富" in preference and country in ["西班牙", "墨西哥", "葡萄牙"]:
            score += 6
        if "交通便利" in preference and country in ["葡萄牙", "西班牙"]:
            score += 6
        if "自然风光" in preference and country in ["克罗地亚", "泰国"]:
            score += 6
        if "夜生活" in preference and country in ["泰国", "墨西哥", "西班牙"]:
            score += 5
        if "购物方便" in preference and country in ["泰国", "葡萄牙", "西班牙"]:
            score += 5
        if "运动设施" in preference and country in ["泰国", "克罗地亚", "西班牙"]:
            score += 5
        
        # 自定义偏好AI分析（简化版）
        if custom_preference:
            custom_pref_lower = custom_preference.lower()
            
            # 关键词匹配
            if any(word in custom_pref_lower for word in ['滑雪', '雪山', '冬季运动']) and country in ["克罗地亚"]:
                score += 7
            if any(word in custom_pref_lower for word in ['瑜伽', '冥想', '静心']) and country in ["泰国", "葡萄牙", "克罗地亚"]:
                score += 6
            if any(word in custom_pref_lower for word in ['潜水', '冲浪', '海岛']) and country in ["泰国", "克罗地亚"]:
                score += 7
            if any(word in custom_pref_lower for word in ['学校', '教育', '孩子']) and country in ["葡萄牙", "西班牙"]:
                score += 8
            if any(word in custom_pref_lower for word in ['创业', '商业', '投资']) and country in ["葡萄牙", "泰国", "墨西哥"]:
                score += 6
            if any(word in custom_pref_lower for word in ['艺术', '设计', '创意']) and country in ["西班牙", "葡萄牙", "墨西哥"]:
                score += 6
            if any(word in custom_pref_lower for word in ['安静', '宁静', '人少']) and country in ["克罗地亚", "泰国"]:
                score += 6
            if any(word in custom_pref_lower for word in ['热闹', '繁华', '社交']) and country in ["泰国", "墨西哥", "西班牙"]:
                score += 6
        
        # 家庭情况
        family = user_profile.get("family", "单身")
        if family == "单身":
            if country in ["泰国", "墨西哥", "克罗地亚"]:
                score += 5
        elif family == "情侣":
            if country in ["葡萄牙", "西班牙"]:
                score += 5
        elif family == "带娃":
            if country in ["葡萄牙", "西班牙", "泰国"]:
                score += 8  # 带娃家庭权重更高
        
        # 职业匹配 - 支持自定义职业
        job = user_profile.get("job", "")
        custom_job = user_profile.get("custom_job", "")
        
        # 标准职业匹配
        if "程序员" in job or "设计师" in job:
            if country in ["泰国", "葡萄牙", "克罗地亚"]:
                score += 5
        if "自媒体" in job:
            if country in ["泰国", "墨西哥", "西班牙"]:
                score += 6
        if "咨询顾问" in job:
            if country in ["葡萄牙", "西班牙", "克罗地亚"]:
                score += 5
        
        # 自定义职业AI分析（简化版）
        if custom_job:
            job_lower = custom_job.lower()
            
            # 关键词匹配
            if any(word in job_lower for word in ['写作', '作家', '作者', '翻译']) and country in ["泰国", "墨西哥", "葡萄牙"]:
                score += 6
            if any(word in job_lower for word in ['教育', '教学', '老师', '在线课程']) and country in ["泰国", "葡萄牙", "西班牙"]:
                score += 6
            if any(word in job_lower for word in ['营销', '推广', '社交媒体', '电商']) and country in ["泰国", "墨西哥", "西班牙"]:
                score += 6
            if any(word in job_lower for word in ['艺术', '设计', '创意', '摄影']) and country in ["西班牙", "葡萄牙", "墨西哥"]:
                score += 6
            if any(word in job_lower for word in ['技术', '开发', '编程', '软件']) and country in ["泰国", "葡萄牙", "克罗地亚"]:
                score += 5
            if any(word in job_lower for word in ['金融', '交易', '投资']) and country in ["葡萄牙", "西班牙", "克罗地亚"]:
                score += 5
        
        data["匹配度"] = min(score, 100)
        matches.append((country, data))
    
    # 按匹配度排序
    matches.sort(key=lambda x: x[1]["匹配度"], reverse=True)
    return matches

def main():
    # 主界面
    st.title("🌍 数字游民签证助手")
    st.subheader("AI帮你找到最适合的数字游民目的地")
    
    # 创建两栏布局
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.header("📝 填写信息")
        
        # 用户输入表单
        with st.form("user_profile_form"):
            job = st.selectbox(
                "职业",
                ["程序员", "设计师", "自媒体", "咨询顾问", "其他"]
            )
            
            # 如果选择了"其他"，显示自定义输入框
            custom_job = ""
            if job == "其他":
                custom_job = st.text_input(
                    "请描述您的职业",
                    placeholder="例如：作家、翻译、在线教育、数字营销等..."
                )
            
            monthly_income = st.number_input(
                "月收入（人民币）",
                min_value=0,
                max_value=100000,
                value=20000,
                step=1000
            )
            
            continent = st.selectbox(
                "目标大洲",
                ["欧洲", "东南亚", "美洲"]
            )
            
            preference = st.multiselect(
                "偏好（可多选）",
                [
                    "海滩", "城市", "低成本", "安全", "网络好",
                    "气候温和", "华人社区", "英语普及", "教育资源", 
                    "医疗水平", "美食丰富", "文化丰富", "交通便利",
                    "自然风光", "夜生活", "购物方便", "运动设施", "其他"
                ]
            )
            
                        
            # 如果选择了"其他"，显示自定义输入框
            custom_preference = ""
            if "其他" in preference:
                custom_preference = st.text_area(
                    "请描述您的其他偏好（可选）",
                    placeholder="例如：喜欢滑雪、需要华人学校、重视瑜伽馆等...",
                    height=100
                )
            
            family = st.selectbox(
                "家庭情况",
                ["单身", "情侣", "带娃"]
            )
            
            submitted = st.form_submit_button("🚀 获取推荐", type="primary")
    
    with col2:
        if submitted:
            st.header("🎯 推荐结果")
            
            # 准备用户数据
            user_profile = {
                "job": job,
                "custom_job": custom_job,
                "monthly_income": monthly_income,
                "continent": continent,
                "preference": ",".join(preference),
                "custom_preference": custom_preference,
                "family": family
            }
            
            # 计算匹配度
            matches = calculate_match(user_profile)
            
            # 显示Top 3推荐
            for i, (country, data) in enumerate(matches[:3]):
                if i == 0:
                    st.success(f"### 🥇 第{i+1}推荐：{country}（匹配度：{data['匹配度']}%）")
                elif i == 1:
                    st.info(f"### 🥈 第{i+1}推荐：{country}（匹配度：{data['匹配度']}%）")
                else:
                    st.warning(f"### 🥉 第{i+1}推荐：{country}（匹配度：{data['匹配度']}%）")
                
                # 显示详细信息
                tab1, tab2, tab3 = st.tabs(["核心优势", "关键门槛", "成本预估"])
                
                with tab1:
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.markdown("**✅ 优势：**")
                        for adv in data["优势"]:
                            st.markdown(f"- {adv}")
                    with col_b:
                        st.markdown("**❌ 劣势：**")
                        for dis in data["劣势"]:
                            st.markdown(f"- {dis}")
                
                with tab2:
                    st.markdown(f"**签证类型：** {data['签证类型']}")
                    st.markdown(f"**收入要求：** {data['收入要求']}")
                    st.markdown(f"**存款要求：** {data['存款要求']}")
                    st.markdown(f"**处理时间：** {data['处理时间']}")
                
                with tab3:
                    st.markdown(f"**每月生活费：** {data['每月生活费']}")
                    st.markdown(f"**税率：** {data['税率']}")
                    
                    # 计算年度成本
                    monthly_cost = int(data['每月生活费'].replace('€', '').replace('$', '').split('-')[0])
                    annual_cost = monthly_cost * 12
                    st.markdown(f"**预估年成本：** €{annual_cost:,}")
                
                st.markdown("---")
                
                # 付费解读部分
                st.markdown("### 🔒 深度解读（付费内容）")
                st.info("💡 解锁完整指南，获取详细实操信息")
                
                # 检查是否已解锁
                if f'unlocked_{country}' not in st.session_state:
                    st.session_state[f'unlocked_{country}'] = False
                
                if not st.session_state[f'unlocked_{country}']:
                    # 显示付费内容预览
                    with st.expander("📋 查看包含内容（点击展开）"):
                        st.markdown("**解锁后将获得：**")
                        st.markdown("- ✅ 资格与材料详解（职业要求、收入形式、核心材料清单）")
                        st.markdown("- ✅ 生活与保障指南（医疗、住房、家庭随行、教育）")
                        st.markdown("- ✅ 税务与身份规划（税务政策、居住要求、入籍路径）")
                        st.markdown("- ✅ 风险与注意事项（签证期限、常见坑点、出入境注意）")
                    
                    # 解锁按钮
                    if st.button(f"🔓 解锁{country}完整指南", key=f"unlock_btn_{country}"):
                        # 这里可以接入实际支付流程
                        # 暂时使用模拟支付
                        st.info("🔄 正在跳转到支付页面...")
                        st.session_state['payment_country'] = country
                        st.session_state['payment_amount'] = 99  # 99元/国家
                        st.session_state['show_payment'] = True
                        st.rerun()
                else:
                    # 显示已解锁的付费内容
                    st.success(f"✅ {country}完整指南已解锁")
                    
                    # 付费内容标签页
                    premium_tabs = st.tabs(["资格与材料", "生活与保障", "税务与身份", "风险与注意事项"])
                    
                    with premium_tabs[0]:
                        st.markdown("**职业要求：**")
                        st.write(data['付费解读']['资格与材料']['职业要求'])
                        st.markdown("**收入形式：**")
                        st.write(data['付费解读']['资格与材料']['收入形式'])
                        st.markdown("**核心材料清单：**")
                        for item in data['付费解读']['资格与材料']['核心材料']:
                            st.markdown(f"- {item}")
                        st.markdown("**材料时效性：**")
                        st.write(data['付费解读']['资格与材料']['材料时效'])
                    
                    with premium_tabs[1]:
                        st.markdown("**医疗保障：**")
                        st.write(data['付费解读']['生活与保障']['医疗保障'])
                        st.markdown("**住房情况：**")
                        st.write(data['付费解读']['生活与保障']['住房情况'])
                        st.markdown("**家庭随行：**")
                        st.write(data['付费解读']['生活与保障']['家庭随行'])
                        if '教育资源' in data['付费解读']['生活与保障']:
                            st.markdown("**教育资源：**")
                            st.write(data['付费解读']['生活与保障']['教育资源'])
                        if '华人社区' in data['付费解读']['生活与保障']:
                            st.markdown("**华人社区：**")
                            st.write(data['付费解读']['生活与保障']['华人社区'])
                        if '季节影响' in data['付费解读']['生活与保障']:
                            st.markdown("**季节影响：**")
                            st.write(data['付费解读']['生活与保障']['季节影响'])
                    
                    with premium_tabs[2]:
                        st.markdown("**税务政策：**")
                        st.write(data['付费解读']['税务与身份']['税务政策'])
                        st.markdown("**居住要求：**")
                        st.write(data['付费解读']['税务与身份']['居住要求'])
                        if '入籍优势' in data['付费解读']['税务与身份']:
                            st.markdown("**入籍优势：**")
                            st.write(data['付费解读']['税务与身份']['入籍优势'])
                        if '入籍要求' in data['付费解读']['税务与身份']:
                            st.markdown("**入籍要求：**")
                            st.write(data['付费解读']['税务与身份']['入籍要求'])
                        if '身份优势' in data['付费解读']['税务与身份']:
                            st.markdown("**身份优势：**")
                            st.write(data['付费解读']['税务与身份']['身份优势'])
                        if '签证限制' in data['付费解读']['税务与身份']:
                            st.markdown("**签证限制：**")
                            st.write(data['付费解读']['税务与身份']['签证限制'])
                    
                    with premium_tabs[3]:
                        st.markdown("**签证期限：**")
                        st.write(data['付费解读']['风险与注意事项']['签证期限'])
                        st.markdown("**常见坑点：**")
                        for pitfall in data['付费解读']['风险与注意事项']['常见坑点']:
                            st.markdown(f"- ⚠️ {pitfall}")
                        st.markdown("**出入境注意：**")
                        st.write(data['付费解读']['风险与注意事项']['出入境注意'])
                        st.markdown("**续签要点：**")
                        st.write(data['付费解读']['风险与注意事项']['续签要点'])
            
            # 显示用户输入摘要
            with st.expander("📊 查看您的输入信息"):
                # 显示职业信息（包含自定义职业）
                job_display = user_profile["job"]
                if user_profile.get("custom_job"):
                    job_display = f"{user_profile['job']}（自定义：{user_profile['custom_job']}）"
                
                st.markdown(f"**职业：** {job_display}")
                st.markdown(f"**月收入：** {user_profile['monthly_income']} 人民币")
                st.markdown(f"**目标大洲：** {user_profile['continent']}")
                st.markdown(f"**偏好：** {user_profile['preference']}")
                if user_profile.get("custom_preference"):
                    st.markdown(f"**自定义偏好：** {user_profile['custom_preference']}")
                st.markdown(f"**家庭情况：** {user_profile['family']}")
        
        else:
            st.info("👈 请在左侧填写信息，获取个性化推荐")
            
            # 显示示例
            st.markdown("### 📝 示例")
            st.markdown("**职业：** 程序员")
            st.markdown("**月收入：** 25000人民币")
            st.markdown("**目标大洲：** 欧洲")
            st.markdown("**偏好：** 安全、网络好")
            st.markdown("**家庭情况：** 单身")
    
    # 添加页脚
    st.markdown("---")
    st.markdown("🚀 MVP版本 | 数据更新于2026年 | 仅供参考，具体政策请以官方为准")

# 支付页面（模态框效果）
if 'show_payment' in st.session_state and st.session_state['show_payment']:
    st.markdown("---")
    st.markdown("## 💳 支付页面")
    
    country = st.session_state.get('payment_country', '')
    amount = st.session_state.get('payment_amount', 99)
    
    st.markdown(f"### 解锁 {country} 完整指南")
    st.markdown(f"#### 价格：¥{amount}")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("**支付方式：**")
        payment_method = st.radio("选择支付方式", ["微信支付", "支付宝"])
        
        if payment_method == "微信支付":
            st.markdown("**请使用微信扫描二维码支付：**")
            # 这里可以显示真实的支付二维码
            st.image("https://via.placeholder.com/300x300.png?text=微信支付二维码", width=200)
        else:
            st.markdown("**请使用支付宝扫描二维码支付：**")
            st.image("https://via.placeholder.com/300x300.png?text=支付宝二维码", width=200)
        
        st.markdown("**支付说明：**")
        st.markdown("- 支付成功后，完整指南将立即解锁")
        st.markdown("- 您可以随时查看已解锁的内容")
        st.markdown("- 支持7天无理由退款")
    
    with col2:
        st.markdown("**订单信息：**")
        st.markdown(f"- 商品：{country}完整指南")
        st.markdown(f"- 价格：¥{amount}")
        st.markdown(f"- 有效期：永久")
        
        # 模拟支付按钮
        if st.button("✅ 确认已支付", type="primary"):
            # 模拟支付成功
            st.success("🎉 支付成功！正在解锁内容...")
            
            # 解锁对应国家的付费内容
            st.session_state[f'unlocked_{country}'] = True
            
            # 清除支付状态
            del st.session_state['show_payment']
            del st.session_state['payment_country']
            del st.session_state['payment_amount']
            
            # 重新加载页面
            st.rerun()
        
        if st.button("❌ 取消支付"):
            # 取消支付
            del st.session_state['show_payment']
            del st.session_state['payment_country']
            del st.session_state['payment_amount']
            st.rerun()

if __name__ == "__main__":
    main()
