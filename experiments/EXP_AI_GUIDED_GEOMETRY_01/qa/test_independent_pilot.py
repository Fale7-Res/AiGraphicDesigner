# START CHANGE AGD-AGENTIC-QA-PILOT | 2026-10-31T14:55:00Z | EDITED | Author: agentic_qa
"""Provider-loop parser/allowlist controls with fake responses only."""
from pathlib import Path
import sys
import unittest

EXPERIMENT = Path(r'C:\Users\Mohamed\Desktop\AiGraphicDesigner\experiments\EXP_AI_GUIDED_GEOMETRY_01')
sys.path.insert(0,str(EXPERIMENT))
from groq_pilot import strict_call_arguments


class IndependentPilotParserAudit(unittest.TestCase):
    def test_reject_duplicate_keys_nonfinite_or_nested_overflow(self):
        for text in ['{"roi":[0,0,1,1],"roi":[0,0,0.5,0.5]}',
                     '{"value":NaN}', '{"value":Infinity}',
                     '['*1100+'0'+']'*1100,
                     '{"value":"'+'x'*2048+'"}']:
            with self.subTest(prefix=text[:30]),self.assertRaises(ValueError):
                strict_call_arguments(text)

    def test_valid_json_is_data_not_execution(self):
        parsed = strict_call_arguments('{"command":"do not execute","trace_ids":[1,2]}')
        self.assertEqual(parsed,{'command':'do not execute','trace_ids':[1,2]})
        # Engine closed schema, rather than parsing, is the execution boundary.


if __name__ == '__main__':
    unittest.main()
# END CHANGE AGD-AGENTIC-QA-PILOT | 2026-10-31T14:55:00Z | EDITED | Author: agentic_qa
