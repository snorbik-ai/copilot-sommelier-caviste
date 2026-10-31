import React from 'react';
import { StatusBadge } from '../primitives/StatusBadge';

export interface CopilotCockpitProps {
  completionRate: number;
  confirmedFacts: Record<string, any>;
  nextQuestion?: string;
}

export const CopilotCockpit: React.FC<CopilotCockpitProps> = ({ completionRate, confirmedFacts, nextQuestion }) => {
  return (
    <div className="p-4 rounded-xl border border-slate-200 bg-white shadow-sm space-y-4">
      <div className="flex items-center justify-between">
        <h3 className="font-bold text-slate-900 text-base">🤖 Copilot Sommelier & Accords Vins</h3>
        <StatusBadge status={completionRate === 100 ? 'VALIDATED' : 'COLLECTING'} />
      </div>
      <p className="text-xs text-slate-600">Conseiller caviste expert guidant les clients dans le choix d'un vin selon leurs plats et leur budget.</p>
      <div className="space-y-1">
        <div className="flex justify-between text-xs font-medium text-slate-700">
          <span>Complétude FSM</span>
          <span>{completionRate}%</span>
        </div>
        <div className="w-full bg-slate-100 rounded-full h-2 overflow-hidden">
          <div className="bg-emerald-500 h-2 rounded-full transition-all duration-300" style={{ width: `${completionRate}%` }} />
        </div>
      </div>
      {nextQuestion && (
        <div className="p-3 bg-blue-50 rounded-lg border border-blue-100 text-xs text-blue-900">
          <span className="font-semibold block mb-0.5">Question :</span>
          {nextQuestion}
        </div>
      )}
    </div>
  );
};
